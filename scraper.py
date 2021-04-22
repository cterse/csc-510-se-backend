
def Scraper(url):
    from recipe_scrapers import scrape_me
    try:
        scraper = scrape_me(url)

        ingredients_text = ""
        for i,n in enumerate(scraper.ingredients()):
            ingredients_text += str(i+1)  + ") " + n + "\n"
            
        resp = {
            "title": scraper.title(),
            "time": scraper.total_time(),
            "instructions": scraper.instructions(),
            "ingredients": ingredients_text,
            "image_uri":scraper.image(),
            "error": "None"
        }

        return resp
    except:
        
        return {"error": 'Link invalid'}

if __name__ == "__main__":
    print(Scraper("https://www.acouplecooks.com/salmon-and-asparagus/"))