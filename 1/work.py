# 创建递归出错示例 h(2,3) 的树状图

G2 = nx.DiGraph()

# 添加节点和边，展示无限递归趋势（只画一部分）
G2.add_edge("h(2,3)", "h(1,2)")
G2.add_edge("h(2,3)", "h(1,3)")
G2.add_edge("h(1,2)", "h(0,1)")
G2.add_edge("h(1,2)", "h(0,2)")
G2.add_edge("h(1,3)", "h(0,2)_b")
G2.add_edge("h(1,3)", "h(0,3)")

# 标注说明
labels2 = {
    "h(2,3)": "h(2,3)",
    "h(1,2)": "h(1,2)",
    "h(1,3)": "h(1,3)",
    "h(0,1)": "h(0,1)",
    "h(0,2)": "h(0,2)",
    "h(0,2)_b": "h(0,2)",
    "h(0,3)": "h(0,3)"
}

# 绘图
plt.figure(figsize=(10, 6))
pos2 = nx.nx_agraph.graphviz_layout(G2, prog='dot')
nx.draw(G2, pos2, with_labels=False, arrows=True, node_size=2500, node_color="#ffe0e0")
nx.draw_networkx_labels(G2, pos2, labels=labels2, font_size=10)
plt.title("Incorrect Recursion Tree for h(2,3): No Base Case for n < k", fontsize=13)
plt.axis('off')
plt.tight_layout()
plt.show()
