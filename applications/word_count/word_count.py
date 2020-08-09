def word_count(s):
    # Your code here

    cache = {}

    for word in s.split():
        word = word.lower()

        punctuation = '":;,.-+=/\\|[]{}()*^&'
        for ele in word:
            if ele in punctuation:
                word = word.replace(ele, "")

        if word in cache:
            cache[word] += 1

        elif word != '':
            cache.update({ word: 1 })

    return cache


print(word_count("let's go out!"))
# if __name__ == "__main__":
#     # print(word_count(""))
#     print(word_count("Hello"))
#     print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
#     print(word_count('This is a test of the emergency broadcast network. This is only a test.'))