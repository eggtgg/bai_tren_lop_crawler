# Các thư viện cần thiết
import requests
from bs4 import BeautifulSoup


# CÁC HÀM CẦN THIẾT

# HÀM ĐỌC NỘI DUNG CỦA TRANG WEB THEO URL CHỈNH ĐỊNH
# KẾT QUẢ TRẢ VỀ LÀ 1 VĂN BẢN DẠNG CHUỔI
def doc_noi_dung(url):
    raw_page = requests.get(url)
    pass


# HÀM LẤY CÁC ĐƯỜNG LINK WEB TRONG NỘI DUNG ĐỌC VỀ
# KẾT QUẨ TRẢ VỀ LÀ 1 LIST CHỨA CÁC ĐƯỜNG LINK
def lay_cac_duong_link(content):
    pass


# HÀM KIỂM TRA TÍNH HỢP LỆ CỦA 1 ĐƯỜNG LINK
# KẾT QUẢ TRẢ VỀ: True nếu hợp lệ, False nếu không hợp lệ
def chinh_sua_link(item):
    pass


def kiem_tra_link(item):
    pass
