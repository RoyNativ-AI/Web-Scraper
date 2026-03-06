#!/usr/bin/env python3
"""
Test Undetected ChromeDriver to bypass Incapsula on REDACTED.co.il
"""
import undetected_chromedriver as uc
import time

def test_REDACTED():
    url = "https://REDACTED.co.il/קינוחים/מחבתות/פנקייק/פנקייק-עם-קוטג-מופחת-נתרן/"

    print(f"🧪 Testing Undetected ChromeDriver on REDACTED.co.il")
    print(f"URL: {url}\n")

    # Configure options
    options = uc.ChromeOptions()
    # options.add_argument('--headless=new')  # Uncomment to run headless

    print("🚀 Launching Chrome...")
    driver = uc.Chrome(options=options, version_main=None)  # Auto-detect Chrome version

    try:
        print("🌐 Navigating to page...")
        driver.get(url)

        # Wait for page to load
        time.sleep(5)  # Give Incapsula time to challenge

        # Get page source
        content = driver.page_source

        print(f"\n📄 Fetched {len(content)} characters\n")

        # Check for Incapsula block
        if 'Incapsula' in content or '_Incapsula_Resource' in content:
            print("❌ BLOCKED by Incapsula")
            print(f"\nFirst 500 characters:\n{'-'*80}")
            print(content[:500])
            print(f"{'-'*80}")
        else:
            print("✅ SUCCESS! No Incapsula block detected!\n")

            # Check for recipe content
            if 'המרכיבים' in content:
                print("✅ Found 'המרכיבים' (Ingredients)!")

            if 'הוראות הכנה' in content:
                print("✅ Found 'הוראות הכנה' (Instructions)!")

            # Get page title
            title = driver.title
            print(f"\n📋 Page title: {title}")

            # Try to find ingredients
            try:
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(content, 'html.parser')

                print(f"\n🔍 Looking for ingredients...")
                ingredient_items = soup.find_all('li')
                if ingredient_items:
                    print(f"Found {len(ingredient_items)} list items")
                    count = 0
                    for item in ingredient_items:
                        text = item.get_text(strip=True)
                        if text and len(text) < 100 and count < 5:
                            print(f"  {count+1}. {text}")
                            count += 1
            except Exception as e:
                print(f"Could not parse ingredients: {e}")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        print("\n🔒 Closing browser...")
        driver.quit()

if __name__ == "__main__":
    test_REDACTED()
