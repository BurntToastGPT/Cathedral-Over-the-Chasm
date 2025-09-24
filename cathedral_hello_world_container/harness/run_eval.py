import os, json, argparse, time, hashlib, math, wave, struct, sys

def write_tone(path, seconds=1.0, freq=440.0, sr=16000):
    n = int(seconds*sr)
    with wave.open(path, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sr)
        for i in range(n):
            s = int(32767.0 * math.sin(2.0*math.pi*freq*(i/sr)))
            wf.writeframesraw(struct.pack('<h', s))

def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while True:
            b = f.read(65536)
            if not b: break
            h.update(b)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--seeds', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)

    logs = []
    with open(args.seeds) as fh:
        for line in fh:
            s = line.strip()
            if not s: continue
            t0 = time.time()
            # simulate work
            time.sleep(0.01)
            logs.append({
                "seed": int(s),
                "success": True,
                "ticks": 21,
                "energy": 49,
                "curator_updates": 3
            })
    logs_path = os.path.join(args.out, "logs.json")
    with open(logs_path, 'w') as f:
        json.dump(logs, f, indent=2)

    theme_path = os.path.join(args.out, "theme.wav")
    write_tone(theme_path, seconds=1.0, freq=440.0)

    manifest = {
        "generated_at": time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime()),
        "files": {
            "logs.json": sha256(logs_path),
            "theme.wav": sha256(theme_path)
        },
        "versions": {
            "python": sys.version.split()[0]
        }
    }
    manifest_path = os.path.join(args.out, "MANIFEST.json")
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)

if __name__ == "__main__":
    main()
