import pafy
def download_url(url):
    print("eeeeooooo")
    video = pafy.new(url)
    best = video.getbest(preftype = "mp4")
    best.download(quiet = False)
