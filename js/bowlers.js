const puppeteer = require('puppeteer');
const fs = require('fs');

// Function to scrape data for each year
async function scrapeData(year) {
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();

    try {
        console.log(`Navigating to ${year} page...`);
        await page.goto(`https://www.iplt20.com/stats/${year}`, { waitUntil: 'domcontentloaded' });

        // Wait for the bowlers' list to be visible (adjust selector as needed)
        console.log(`Waiting for content to load for ${year}...`);
        await page.waitForSelector('.cSBListItems', { visible: true, timeout: 60000 });

        // Scrape the Purple Cap holder name (or adjust based on exact location)
        const purpleCapName = await page.evaluate(() => {
            const purpleCapSection = document.querySelector(".cSBListItems.bowlers.ng-binding.ng-scope.selected.selected1");
            return purpleCapSection ? purpleCapSection.innerText.trim() : 'No data available';
        });

        console.log(`Purple Cap holder for ${year}: ${purpleCapName}`);

        // Create data object for the year
        const data = {
            year: year,
            purpleCapHolder: purpleCapName
        };

        // Save the data to a JSON file (you can change to CSV or any other format if preferred)
        fs.appendFileSync('purple_cap_data.json', JSON.stringify(data) + '\n');
        console.log(`Data for ${year} saved successfully.`);

    } catch (error) {
        console.error(`Error scraping data for ${year}:`, error);
    } finally {
        await browser.close();
    }
}

// Loop through the years and scrape the data
async function scrapeAllYears() {
    for (let year = 2008; year <= 2023; year++) {
        await scrapeData(year);
    }
}

// Start the scraping process
scrapeAllYears().then(() => {
    console.log('Data scraping completed.');
}).catch(error => {
    console.error('Error during scraping process:', error);
});
