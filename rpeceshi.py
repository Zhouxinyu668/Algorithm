 
import torch
import torch.nn as nn

class RelativePositionSelfAttention(nn.Module):
    def __init__(self, d_model, nhead, seq_len):
        super(RelativePositionSelfAttention, self).__init__()
        self.d_model = d_model  # 输入序列的维度
        self.nhead = nhead  # 注意力头的数量
        self.seq_len = seq_len  # 输入序列的长度
        self.d_k = d_model // nhead  # 每个注意力头的维度

        # 定义线性层用于计算 Q, K, V
        self.WQ = nn.Linear(d_model, d_model)
        self.WK = nn.Linear(d_model, d_model)
        self.WV = nn.Linear(d_model, d_model)
        # 定义线性层用于输出
        self.fc = nn.Linear(d_model, d_model)

        # 定义相对位置编码的 Embedding 层
        self.relative_pos_emb = nn.Embedding(2 * seq_len - 1, self.d_k)

    def forward(self, x):
        # x shape: (batch_size, seq_len, d_model)
        batch_size, seq_len, _ = x.size()

        # 计算 Q, K, V
        Q = self.WQ(x).view(batch_size, seq_len, self.nhead, self.d_k).transpose(1, 2)
        K = self.WK(x).view(batch_size, seq_len, self.nhead, self.d_k).transpose(1, 2)
        V = self.WV(x).view(batch_size, seq_len, self.nhead, self.d_k).transpose(1, 2)

        # 计算相对位置编码
        pos_indices = torch.arange(0, 2 * seq_len - 1, device=x.device)
        pos_embeddings = self.relative_pos_emb(pos_indices)

        # 计算注意力得分
        S = torch.matmul(Q, K.transpose(-1, -2)) / (self.d_k ** 0.5)

        # 计算相对位置得分
        S_rel = torch.matmul(Q.unsqueeze(-2), pos_embeddings.unsqueeze(0).transpose(-1, -2))
        S_rel = S_rel.view(batch_size, self.nhead, seq_len, 2 * seq_len - 1)

        # 将相对位置得分平移以对齐序列
        S_rel_shift = torch.zeros_like(S)
        for i in range(seq_len):
            for j in range(seq_len):
                S_rel_shift[..., i, j] = S_rel[..., i, j - i + seq_len - 1]

        # 计算注意力权重
        A = torch.softmax(S + S_rel_shift, dim=-1)

        # 应用注意力权重
        x = torch.matmul(A, V)

        # 拼接多个注意力头
        x = x.transpose(1, 2).contiguous().view(batch_size, seq_len, -1)

        # 返回最终结果
        return self.fc(x)


rps = RelativePositionSelfAttention(d_model=15,nhead=3, seq_len=5)
b_tensor = torch.Tensor(1,5,15)
a = rps(b_tensor)