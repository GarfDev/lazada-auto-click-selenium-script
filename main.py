import time
import datetime
import random
import warnings
import threading
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

link_list = [
    "https://www.lazada.vn/products/hu-thu-tinh-dung-gia-vi-nha-bep-kem-muong-muc-mau-moi-hu-dung-gia-vi-thuy-tinh-kem-muong-lo-dung-gia-vi-co-nap-kem-thia-muc-i980956585-s3102418891.html?dsource=share&laz_share_info=29064653_100_100_200099193016_25761090_null&laz_token=f9080e1b19ae11635397d9e3ad68d27f",
    "https://www.lazada.vn/products/ke-cai-dao-thot-inox-gs-5004-gia-cai-duadaothot-inox-ke-gac-dao-thot-bang-inox-da-nang-tien-loi-ke-cai-dao-thot-inox-co-moc-treo-i937858359-s2826972042.html?dsource=share&laz_share_info=29064149_100_100_200099193016_25760586_null&laz_token=1d446352dccf67c187d49a36caf7c1c8",
    "https://www.lazada.vn/products/pin-30000mah-sac-nhanh-sac-du-phong-mat-guong-thiet-ke-sang-trong-dung-luong-lon-30000mah-pin-du-phong-co-2-cong-ra-den-led-sieu-sang-mat-pin-guong-co-hien-thi-lcd-phan-tram-pin-sieu-dep-i915494550-s2701360316.html?dsource=share&laz_share_info=29064729_100_100_200099193016_25761166_null&laz_token=7282eb298aedae7695407ccfba3fc7a1",
    "https://www.lazada.vn/products/sale-han-che-nuoc-xa-bong-vang-vao-tai-mat-be-mu-thong-minh-tien-loi-nhieu-mau-sac-non-goi-dau-chan-nuoc-cho-be-i1033108941-s3478424085.html?dsource=share&laz_share_info=29065051_100_100_200099193016_25761488_null&laz_token=f21bd7c71bc660d9a49104376db3c5f6",
    "https://www.lazada.vn/products/dung-ca-ngay-khong-lo-het-pin-tai-nghe-blueooth-cao-cap-tai-nghe-bluetooth-ssopxm-dung-cho-moi-dong-dien-thoai-ipad-thong-minh-tai-nghe-nhet-tai-1-ben-khong-day-chong-on-hieu-qua-to-ro-i872584907-s2494594204.html?dsource=share&laz_share_info=29065256_100_100_200099193016_25761693_null&laz_token=291f7d02cdc7add4ae4ba3c1e91031cd",
    "https://www.lazada.vn/products/cao-cap-ke-de-giay-dep-5-tang-co-ngan-keo-tien-loi-ke-go-cao-cap-de-giay-dep-5-tang-tien-loi-i871762882-s2489540697.html?dsource=share&laz_share_info=29065314_100_100_200099193016_25761751_null&laz_token=bbcf7f1d7844ccf534c84bb7ee0ff65c",
    "https://www.lazada.vn/products/kieng-chan-gio-bep-ga-cao-cap-giup-chia-deu-lua-kieng-chan-gio-bep-gas-nhieu-chaumau-bac-i982632568-s3110578179.html?dsource=share&laz_share_info=29065351_100_100_200099193016_25761788_null&laz_token=d0248cc070f1b53fb62c2398e9f47a6f",
    "https://www.lazada.vn/products/sieu-ben-ke-nhua-gac-bon-rua-chen-thong-minh-co-the-dieu-chinh-kich-co-ke-dung-xa-bong-mieng-rua-chenkem-gia-treo-khan-tien-loi-i902718791-s2621760073.html?dsource=share&laz_share_info=29065414_100_100_200099193016_25761851_null&laz_token=44d8ea49c27ce667113e8c92ee40b8f5",
    "https://www.lazada.vn/products/tang-cap-sac-nhanh-pin-sac-du-phong-ss30-mat-guong-den-sac-cuc-nhanh-cho-nhieu-thiet-bi-cong-nghe-cao-pin-cuc-trau-ben-bi-tuoi-tho-pin-len-den-999-lan-pin-du-phong-pin-sac-du-phong-i872482430-s2492748015.html?dsource=share&laz_share_info=29065462_100_100_200099193016_25761899_null&laz_token=76ed6b2bb6f239186dde5154d58504f4",
    "https://www.lazada.vn/products/ro-nhua-gan-tu-lanh-co-kep-gan-keo-ra-keo-vo-cuc-tien-loi-ke-ro-nhua-dung-thuc-pham-trong-nha-bep-tu-lanh-cuc-tien-dung-chac-chan-i924004636-s2750886606.html?dsource=share&laz_share_info=29065537_100_100_200099193016_25761974_null&laz_token=e50dd2ab0359c77944aa65a25dce81e6",
    "https://www.lazada.vn/products/combo-2-tui-vai-dung-chan-men-quan-ao-tui-vai-dung-chan-men-goi-loai-day-xin-dep-i876704519-s2510256962.html?dsource=share&laz_share_info=29065574_100_100_200099193016_25762011_null&laz_token=bd93a2a805c9e73a3a5432ee1868bf6c",
    "https://www.lazada.vn/products/cao-cap-1form-rong-bo-ao-mua-gom-ao-va-quan-cao-capnguoi-lon-bo-ao-mua-gom-ao-va-quan-nguoi-lon-free-size-duoi-70-ky-gon-nhe-tien-dung-i872696967-s2495170577.html?dsource=share&laz_share_info=29065610_100_100_200099193016_25762047_null&laz_token=3fd357a06fb4556a00450b759ec9b8d6",
    "https://www.lazada.vn/products/nghe-to-ro-dam-thoai-lien-tuc-tai-nghe-bluetooth-nhi-s530-tai-nghe-nho-gon-tien-loi-sieu-tiet-kiem-tai-nghe-bluetooth-mini-nho-gon-chong-on-am-thanh-to-ro-chat-luong-dinh-i872628499-s2494642803.html?dsource=share&laz_share_info=29065682_100_100_200099193016_25762119_null&laz_token=19806dd06ae131440e3be61246a214aa",
    "https://www.lazada.vn/products/hang-chat-luong-micro-danh-cho-loa-bluetooth-micro-hat-karaoke-cao-cap-co-day-micro-hat-karaoke-co-day-danh-cho-loa-thuong-i909762773-s2671046792.html?dsource=share&laz_share_info=29065874_100_100_200099193016_25762311_null&laz_token=3e3e46f402ade323dded3b75c747a740",
    "https://www.lazada.vn/products/sale-hop-do-choi-long-quay-lo-to-bingo-neo-hop-xanh-90-so-sieu-to-sieu-khong-lo-i1049606409-s3573978886.html?dsource=share&laz_share_info=29065979_100_100_200099193016_25762416_null&laz_token=7d02fbafdf293c70124640be30425e44",
    "https://www.lazada.vn/products/kinh-phong-dai-f2-sieu-net-kinh-phong-to-dien-thoai-i698116718-s1733868884.html?dsource=share&laz_share_info=29066132_100_100_200099193016_25762569_null&laz_token=a84cc9b449d9d119b0e8a40b1ca94bf3",
    "https://www.lazada.vn/products/chinh-hang-lan-khu-mui-scion-giai-phap-dut-hoi-nach-hoi-chan-tan-goc-i675798593-s1646658028.html?dsource=share&laz_share_info=29066203_100_100_200099193016_25762640_null&laz_token=a472a50542a47270e586b4bded5a6e59",
    "https://www.lazada.vn/products/dung-luong-20000mah-tang-cap-sac-pin-sac-du-phong-voi-thiet-ke-man-hinh-guong-sang-trong-2-den-led-sieu-sang-sac-nhanh-cho-tat-ca-cac-dt-an-toan-cho-may-sieu-khuyen-mai-i797208566-s2157780735.html?dsource=share&laz_share_info=29066288_100_100_200099193016_25762725_null&laz_token=c9e5f7bdb916503551acfd995c9e7346",
    "https://www.lazada.vn/products/sieu-tien-loi-choi-cha-san-thong-minh-cai-dai-co-be-mat-gat-nuoc-choi-cha-san-sieu-tien-loi-i909382879-s2664628415.html?dsource=share&laz_share_info=29066346_100_100_200099193016_25762783_null&laz_token=ce3300d2f060710a155cc9263671c99f",
    "https://www.lazada.vn/products/dung-luong-30000mah-tang-cap-sac-25k-pin-sac-du-phong-thiet-ke-mat-guong-cao-cap-hien-thi-phan-tram-pin-pin-du-phong-2-cong-sac-ho-tro-sac-nhieu-thiet-bi-cung-luc-i819766729-s2243326974.html?dsource=share&laz_share_info=29066402_100_100_200099193016_25762839_null&laz_token=7ecf1819809b45112844e984aaec266c",
    "https://www.lazada.vn/products/tu-vai-dung-day-dep-ao-quan-5-ngan-6-tangmau-tron-ko-hoa-van-ke-cao-cap-gia-re-tu-vai-che-chan-bui-tien-loi-ke-giay-dep-sieu-ben-chac-i930220258-s2786308661.html?dsource=share&laz_share_info=29066462_100_100_200099193016_25762899_null&laz_token=173c66b0f941fa929e8f37cbeb0e6173",
    "https://www.lazada.vn/products/cao-cap-bo-sac-zin-oppo-4a-fullbox-bo-sac-dien-thoai-cuc-nhanh-vooc-oppo-40-ak779-f9-f9-plus-a37-neo3-neo5-neo7neo9-f1-f1s-f3-plus-f3-a33-2020-i831814593-s2301614289.html?dsource=share&laz_share_info=29066539_100_100_200099193016_25762976_null&laz_token=188661d1a5ad61cb2f4b2f1db68ca033",
    "https://www.lazada.vn/products/sale-sap-san-hang-tot-pin-sac-du-phong-30000mah-mat-kinh-cuong-luc-cao-cap-pin-ben-sac-nhanh-dung-ca-ngay-khong-het-pin-tuoi-tho-pin-hon-999-lan-sac-i726622050-s1847148680.html?dsource=share&laz_share_info=29066647_100_100_200099193016_25763084_null&laz_token=61587c9636fb797ef25a43825745ed45",
    "https://www.lazada.vn/products/nghe-hay-gia-re-tai-nghe-bluetooth-phu-hop-voi-tat-ca-cac-loai-dien-thoai-am-thanh-sieu-chuan-sieu-hay-pin-trau-su-dung-lau-i669610952-s1626400168.html?dsource=share&laz_share_info=29066736_100_100_200099193016_25763173_null&laz_token=0a9974b5b2e5914ed73f9abdd1956ecd",
    "https://www.lazada.vn/products/loai-manh-chai-xit-tay-rua-nha-bep-tay-mang-bam-sieu-nang-kitchen-cleaner-mang-bam-chay-khet-tren-xong-noi-thiet-bi-nha-bep-sach-bong-i705916124-s1761782702.html?dsource=share&laz_share_info=29066936_100_100_200099193016_25763373_null&laz_token=3c0e8986333c0c781e3ae97002ca7e8c",
]


def drag_slider(driver):
    slider = driver.find_element_by_id('nc_2_n1z')
    slider.click()
    ac = ActionChains(driver)
    ac.move_to_element(slider)
    ac.click_and_hold(slider)
    xoffset = 0
    while xoffset < 350:
        xmove = random.randint(10, 40)
        ymove = random.randint(-1, 1)
        ac.move_by_offset(xmove, ymove)
        xoffset += xmove
    ac.release()
    ac.perform()

    time.sleep(3)

    element = driver.find_element_by_class_name('nc-lang-cnt')
    print(element.text)


def runner(chrome_driver, index):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.headless = True
    # options.add_argument(f'user-agent={generate_user_agent()}')

    warnings.filterwarnings('ignore')
    driver = webdriver.Chrome(chrome_driver, chrome_options=options)

    driver.set_window_size(1366, 768)

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
        })
    """
    })

    for x in range(1000):
        print(f"[{datetime.datetime.now()}] Go to product page..")
        driver.get(random.choice(link_list))
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "container")))

        if "captcha" in driver.title:
            print(f"[Thread-{index}] Resolving captcha..")
            drag_slider(driver)

        try:
            time.sleep(random.randint(4, 6))
            element = driver.find_element_by_class_name(
                'add-to-cart-buy-now-btn')
            time.sleep(random.randint(10, 20))
            print(f"[Thread-{index}] Back to main page..")
            driver.get(random.choice(link_list))
            time.sleep(random.randint(10, 20))
        except:
            print(
                f"[{datetime.datetime.now()}] Failed to load product page, sleep for 300 sec..")
            driver.save_screenshot(
                f"./screenshots/{datetime.datetime.now()}.png")
            time.sleep(random.randint(300, 600))

    driver.quit()


if __name__ == "__main__":
    threads = []

    chrome_driver = ChromeDriverManager().install()

    for index in range(10):
        x = threading.Thread(target=runner, args=(chrome_driver, index))
        threads.append(x)
        time.sleep(random.randint(2, 10))
        x.start()
