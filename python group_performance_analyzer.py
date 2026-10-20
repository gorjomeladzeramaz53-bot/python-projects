# დავალება 7: სტუდენტების ქულების დინამიური ანალიზატორი

def analyze_scores():
    scores = []
    print("📊 სტუდენტების ქულების ანალიზატორი ჩაერთო!")
    print("შეიყვანეთ ქულები (0-დან 10-მდე). დასასრულებლად ჩაწერეთ: stop\n")

    while True:
        user_input = input("შეიყვანეთ ქულა ან 'stop': ").strip().lower()

        # ციკლის შეწყვეტა
        if user_input == "stop":
            break

        # Try-Except ბლოკი არასწორი მონაცემების ასაცილებლად
        try:
            score = float(user_input)
            
            # შემოწმება, რომ ქულა არის 0-სა და 10-ს შორის
            if 0 <= score <= 10:
                scores.append(score)
                print(f"შენახულია ქულა: {score}")
            else:
                print("⚠️ გთხოვთ შეიყვანოთ რიცხვი 0-სა და 10-ს შორის!")
                
        except ValueError:
            print("❌ გთხოვთ შეიყვანოთ სწორი რიცხვი ან 'stop'.")

    # თუ სია ცარიელი არ არის, ვაკეთებთ ანალიზს
    if scores:
        min_score = min(scores)
        max_score = max(scores)
        avg_score = sum(scores) / len(scores)
        sorted_scores = sorted(scores)

        print("\n" + "="*40)
        print("📈 ანალიზის შედეგები:")
        print(f"• მინიმალური ქულა: {min_score}")
        print(f"• მაქსიმალური ქულა: {max_score}")
        print(f"• კლასის საშუალო პერფორმანსი: {avg_score:.2f}")
        print(f"• ყველა ქულა ზრდადობით: {sorted_scores}")
        
        print("• თითოეული ქულის განმეორება:")
        # თითოეული ქულის განმეორების (სიხშირის) გამოთვლა
        for s in sorted(set(sorted_scores)):
            count = scores.count(s)
            print(f"  - ქულა {s}: {count} ჯერ")
        print("="*40)
    else:
        print("\n⚠️ ქულები არ შეყვანილა.")

if __name__ == "__main__":
    analyze_scores()