import wikipedia

def main():
    while True:
        title = input("Enter page title: ")
        if not title:
            print("Thank you.")
            break
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print("\nTITLE:", page.title)
            print("SUMMARY:", page.summary[:300], "...")
            print("URL:", page.url)
        except wikipedia.DisambiguationError as e:
            print("\nWe need a more specific title. Try one of the following, or a new search:")
            print(e.options[:5])
        except wikipedia.PageError:
            print(f'\nNo Wikipedia page found for "{title}". Try again.')

if __name__ == '__main__':
    main()
