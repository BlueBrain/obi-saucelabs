from bs4 import BeautifulSoup


class UrlScraper:
    @staticmethod
    def scrape_links(page_source):
        soup = BeautifulSoup(page_source, 'html.parser')
        links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                links.append(href)
        return links

    @staticmethod
    def write_links_to_file(links, file_path, mode='a'):
        with open(file_path, 'a') as f:
            for link in links:
                f.write(link + '\n')
