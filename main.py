from test_bench import TestBench


def main():
    print("🔧 Initializing Test Bench...")
    bench = TestBench()

    print("\n✅ Connected Instruments:")
    instruments = bench.list_all()

    for category, items in instruments.items():
        print(f"\n🔹 {category.replace('_', ' ').title()}:")
        if items:
            for res in items:
                print(f"  - {res}")
        else:
            print("  (None detected)")


if __name__ == "__main__":
    main()
