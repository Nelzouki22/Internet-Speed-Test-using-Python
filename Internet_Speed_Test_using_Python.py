import speedtest

def test_speed():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    st.results.ping
    
    results = st.results.dict()
    download_speed = results["download"] / 1_000_000  # تحويل إلى ميغابت في الثانية
    upload_speed = results["upload"] / 1_000_000  # تحويل إلى ميغابت في الثانية
    ping = results["ping"]
    
    print(f"سرعة التحميل: {download_speed:.2f} ميغابت في الثانية")
    print(f"سرعة الرفع: {upload_speed:.2f} ميغابت في الثانية")
    print(f"البينغ: {ping:.2f} مللي ثانية")

if __name__ == "__main__":
    test_speed()

