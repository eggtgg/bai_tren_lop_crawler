# Các thư viện cần thiết
import taofile
import web

def start():
    #Nhóm các biến toàn cục cung cấp thông số cho chương trình
    url_list = ['https://vietnamnet.vn/'] #Chứa các đường link sẽ được duyệt
    history = [] #Chứa các đường link đã duyệt
    max_page = 1000 # Quy định số lượng các web được  tải về
    count = 0 #Đếm số lượng web đã tải về
    data_folder = "C:\\Minh_Tri_Ho\\python\\crawler"


    #kịch bản tải các trang web
    while (count < max_page) and (len(url_list) > 0):
        url = url_list(pop(0))
        page = web.doc_noi_dung(url)
        link = web.lay_cac_duong_link(page)
        for item in links: # duyệt từng đường link thu được để kiểm tra tính hợp lệ
            if web.kiem_tra_link(item): # nếu đường link là hợp lệ thì tiếp tục thực hiện đoạn lệnh
                item = web.chinh_sua_link(item)
                if not ((item in url_list) and (item in history)):
                    url_list.append(item)
                taofile.luu_noi_dung_xuong_file(page, data_folder)
                history.append(url)
                count += 1


if __name__ == '__main__':
    start()
