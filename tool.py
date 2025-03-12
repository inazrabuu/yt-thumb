import re

class Extractor:
  def __init__(self, url: str):
    self.url = url
    self.url_options = [
      'youtube.com',
      'youtu.be'
    ]

  def get_domain(self) -> str:
    pattern = r"https?://(?:www\.)?([^/]+)"
    match = re.search(pattern, self.url)
    return match.group(1) if match else None

  def get_youtube_code(self) -> str:
    domain = self.get_domain()
    try:
      i = self.url_options.index(domain)
    except ValueError:
      i = -1

    if i == -1:
      return "Unknown Domain"
    
    return self.strip_noise(self.url, i)
  
  def strip_noise(self, url: str, i: int) -> str:
    url_split = url.split('/')
    
    code = url_split[3]
    if i == 0:
      code = code.split('=')[1]
    else:
      code = code.split('?')[0]

    return code
  
import requests
  
class Downloader:
  def __init__(self, url, name):
    self.url = url
    self.name = name

  def get(self):
    response = requests.get(self.url, stream=True)
    img_name = f"{self.name}.jpg"

    if response.status_code == 200:
      with open(img_name, "wb") as f:
        for chunk in response.iter_content(1024):
          f.write(chunk)
      print("Download Complete")
      ret_val = img_name
    else:
      ret_val = "Downlaod failed!"
      print(ret_val)

    return ret_val

