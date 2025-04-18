import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 图片路径和 caption 文本
images = [
    ("static/images/human_mixed_results.png", "Human"),
    ("static/images/gpt4o_mixed.png", "GPT-4o"),
    ("static/images/xcmp_mixed.png", "XComposer")
]

fig, axs = plt.subplots(1, 3, figsize=(12, 4))

for ax, (img_path, caption) in zip(axs, images):
    img = mpimg.imread(img_path)
    ax.imshow(img)
    ax.axis('off')
    ax.set_title(caption, fontsize=10)

plt.tight_layout()
plt.savefig("static/images/merged_wordcloud.png", dpi=300)
