import matplotlib.pyplot as plt

arquivos = ["livroDeRedes.pdf", "clipe_rosalia.mp4", "ep_simpsons.mp4", "joias.pdf"]
tamanhos = [2384082, 22550865, 66811752, 225627318]  # em bytes
tcp_tempos = [17.21, 157.79, 391.11, 1036.32]  # ms
udp_tempos = [37.18, 265.56, 896.02, 3036.9]  # ms

fig, ax1 = plt.subplots(figsize=(10, 6))

# graf barras
ax1.bar(arquivos, tamanhos, color="lightblue", alpha=0.7, label="Tamanho dos Arquivos (bytes)")
ax1.set_xlabel("Nome dos arquivos", fontsize=12)
ax1.set_ylabel("Tamanho dos Arquivos (bytes)", fontsize=12)
ax1.tick_params(axis="y")
ax1.legend(loc="upper left")

# graf lihas
ax2 = ax1.twinx()
ax2.plot(arquivos, tcp_tempos, label="TCP (ms)", color="blue", marker="o")
ax2.plot(arquivos, udp_tempos, label="UDP (ms)", color="red", marker="s")
ax2.set_ylabel("Tempo de Transferência (ms)", fontsize=12)
ax2.tick_params(axis="y")
ax2.legend(loc="upper right")

plt.title("Tamanho dos Arquivos vs Tempo de Transferência (ms)", fontsize=14)
plt.tight_layout()

plt.savefig("grafico.png")
plt.close()
