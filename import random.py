import random

def generate_ip_list(count=100):
    normal_subnet = "192.168.1."
    intruder_subnet = "10.0.0."
    ips = [normal_subnet + str(random.randint(1, 254)) for _ in range(count - 1)]
    intruder_ip = intruder_subnet + str(random.randint(1, 254))
    ips.append(intruder_ip)
    random.shuffle(ips)
    return ips, intruder_ip

def run_ip_mission():
    print("🔍 MISSION: Find the Intruder IP")
    print("One of these IPs does NOT belong to the same subnet. Can you find it?\n")

    ip_list, answer = generate_ip_list(100)

    for i, ip in enumerate(ip_list, 1):
        print(f"{i:3}. {ip}")

    guess = input("\nEnter the suspicious IP address: ").strip()

    if guess == answer:
        print("\n✅ Correct! That IP doesn't belong to the subnet. You found the intruder!")
    else:
        print(f"\n❌ Wrong. The intruder was: {answer}")

if __name__ == "__main__":
    run_ip_mission()