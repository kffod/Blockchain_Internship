import random

# PoW Simulation
pow_validators = [{'id': f'Miner{i}', 'power': random.randint(1, 100)} for i in range(3)]
pow_winner = max(pow_validators, key=lambda x: x['power'])
print("\n🔧 PoW Winner:", pow_winner)
print(f"Selected based on highest computational power: {pow_winner['power']}")

# PoS Simulation
pos_validators = [{'id': f'Staker{i}', 'stake': random.randint(1, 100)} for i in range(3)]
pos_winner = max(pos_validators, key=lambda x: x['stake'])
print("\n💰 PoS Winner:", pos_winner)
print(f"Selected based on highest stake: {pos_winner['stake']}")

# DPoS Simulation
dpos_candidates = ['Alice', 'Bob', 'Charlie']
votes = [random.choice(dpos_candidates) for _ in range(10)]
vote_counts = {c: votes.count(c) for c in dpos_candidates}
dpos_winner = max(vote_counts, key=vote_counts.get)
print("\n🗳️ DPoS Winner:", dpos_winner)
print(f"Selected based on most community votes: {vote_counts[dpos_winner]}")
