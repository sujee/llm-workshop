import json
import random

def generate_sample_data(num_samples):
  """Generates sample data with the specified constraints."""
  data = []
  for _ in range(num_samples):
    name = f"Person{random.randint(1, 1000)}"
    age = random.randint(1, 99)
    gender = random.choice(['M', 'F', 'N'])
    weight = random.uniform(50, 300)  # Adjust range as needed

    if age > 20:
      weight = random.uniform(100, 300)  # Ensure weight >= 100 for ages > 20

    data.append({
        "name": name,
        "age": age,
        "gender": gender,
        "weight": weight
    })
  return data

# Generate 100 samples
samples = generate_sample_data(100)

# Print the generated JSON data
for sample in samples:
  print(json.dumps(sample))