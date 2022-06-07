# sentence translator program
def main():
    print(p1_sentences())

# translating the sentence
def p1_sentences():
    sentence = input("what is sentence? ").strip()
    st = []
    for i in sentence.split():
        if i[0] in "aeiou":
            st.append(i + "way")
        else:
            
            st.append(i[1:] + i[0] + "ay")
    return ' '.join(st)

if __name__ == "__main__":
    main()