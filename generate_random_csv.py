import csv
import random
import pandas as pd

# Number of nodes and edges
num_nodes = 6005
num_edges = 60915
num_channels = num_edges  # Each edge and its counter edge make a channel

# Generate nodes
nodes = [{'id': i} for i in range(num_nodes)]

# Generate edges
edges = []

for i in range(num_edges):
    from_node_id = random.randint(0, num_nodes - 1)
    to_node_id = random.randint(0, num_nodes - 1)
    
    # Ensure from_node_id and to_node_id are different
    while from_node_id == to_node_id:
        to_node_id = random.randint(0, num_nodes - 1)
    
    balance = random.randint(100, 100000000)
    fee_base = random.randint(0, 5000000)
    fee_proportional = random.uniform(0, 100000000)
    min_htlc = random.randint(0, 1000000)
    timelock = random.randint(0, 1008)
    
    edge = {
        'id': i,
        'from_node_id': from_node_id,
        'to_node_id': to_node_id,
        'balance': balance,
        'fee_base': fee_base,
        'fee_proportional': fee_proportional,
        'min_htlc': min_htlc,
        'timelock': timelock
    }
    
    edges.append(edge)

# Generate channels
channels = []

for i in range(num_edges):
    channel = {
        'id': i,
        'edge1_id': i,
        'edge2_id': (i + num_edges) % num_edges,  # Ensure each edge has a corresponding counter edge
        'node1_id': edges[i]['from_node_id'],
        'node2_id': edges[i]['to_node_id'],
        'capacity': random.randint(1100000, 5E+11)
    }
    
    channels.append(channel)

# Write nodes to nodes_ln.csv
with open('nodes_ln.csv', 'w', newline='') as csvfile:
    fieldnames = ['id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for node in nodes:
        writer.writerow(node)

# Write edges to edges_ln.csv
with open('edges_ln.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'from_node_id', 'to_node_id', 'balance', 'fee_base', 'fee_proportional', 'min_htlc', 'timelock']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for edge in edges:
        writer.writerow(edge)

# Write channels to channels_ln.csv
with open('channels_ln.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'edge1_id', 'edge2_id', 'node1_id', 'node2_id', 'capacity']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for channel in channels:
        writer.writerow(channel)

df = pd.read_csv('edges_ln.csv')
df_sorted = df.sort_values(by='id')
df_sorted.to_csv('edges_ln.csv', index=False)

print("CSV files generated successfully!")
