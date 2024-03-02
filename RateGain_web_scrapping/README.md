
  <h1>RateGain Web Scraping</h1>

  <p>This project is a Python script for web scraping blogs from a website using BeautifulSoup and Selenium. The script extracts blog information such as title, date, image URL, and likes count and saves it to a CSV file.</p>

  <h2>Dependencies</h2>
  <ul>
      <li><a href="https://www.python.org/" target="_blank">Python</a> (>= 3.6)</li>
      <li><a href="https://www.crummy.com/software/BeautifulSoup/" target="_blank">BeautifulSoup</a></li>
      <li><a href="https://www.selenium.dev/documentation/en/" target="_blank">Selenium</a></li>
      <li>Chrome WebDriver (Make sure it is installed and available in the system PATH)</li>
  </ul>

  <h2>Installation</h2>
  <l>Clone the repository:</l>
  <code>git clone https://github.com/your-username/your-repository.git</code>

  <l>Install dependencies:</l>
  <code>pip install -r requirements.txt</code>

  <h2>Usage</h2>
  <p>1. Run the script:<code>python main.py</code>
</p>
  
  <p>2. The script will navigate to the specified URL, scrape blog information, and store it in a CSV file.</p>

  <p>3. The CSV file will be named in the following format: <code>Data_date_YYYY-MM-DD_time_HH_MM_SS.csv</code> </p>
  
  <p>4. A new CSV file will be created in the same directory every time the script runs.</p>

  <h2>Configuration</h2>
  <p>Adjust the script variables as needed:</p>
  <ul>
      <li>URL: Update the <code>url</code> variable with the target website URL.</li>
      <li>Browser: Ensure the correct web driver is installed and configured in the script.</li>
      <li>Output: Customize file names and paths for HTML and CSV files.</li>
  </ul>



  <h2>Acknowledgments</h2>
  <p>Thanks to the developers of BeautifulSoup and Selenium for their excellent tools.</p>

  <hr>

</body>
</html>
