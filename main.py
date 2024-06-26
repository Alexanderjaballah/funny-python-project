def tell_joke():
    joke = pyjokes.get_joke()
    print(f"Here's a funny joke for you: {joke}")

if __name__ == "__main__":
    tell_joke()