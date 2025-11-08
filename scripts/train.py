import argparse, pandas as pd, os

def train(data_path, epochs, save_dir):
    print(f"Loading data from {data_path}")
    df = pd.read_csv(data_path)
    print(f"Sample rows: {len(df)}")
    for e in range(epochs):
        print(f"Epoch {e+1}/{epochs} ... (no-op)")
    os.makedirs(save_dir, exist_ok=True)
    with open(os.path.join(save_dir, "smoke.txt"), "w") as f:
        f.write("smoke run completed\n")
    print("Saved smoke artifact.")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--data", required=True)
    p.add_argument("--epochs", type=int, default=1)
    p.add_argument("--save-dir", default="models/smoke")
    args = p.parse_args()
    train(args.data, args.epochs, args.save_dir)
