class SinhVien:
    def __init__(self, mssv, ho_ten, nam_sinh, chuyen_nganh):
        self.mssv = mssv
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.chuyen_nganh = chuyen_nganh

    def hien_thi_thong_tin(self):
        return f"MSSV: {self.mssv} | Tên: {self.ho_ten} | Năm sinh: {self.nam_sinh} | Ngành: {self.chuyen_nganh}"

class QuanLySinhVien:
    def __init__(self):
        self.danh_sach_sv = []

    def them_sinh_vien(self):
        print("\n--- NHẬP THÔNG TIN SINH VIÊN ---")
        mssv = input("Nhập MSSV: ")
        ho_ten = input("Nhập họ tên: ")
        nam_sinh = input("Nhập năm sinh: ")
        chuyen_nganh = input("Nhập chuyên ngành: ")
        
        sv_moi = SinhVien(mssv, ho_ten, nam_sinh, chuyen_nganh)
        self.danh_sach_sv.append(sv_moi)
        print("=> Thêm sinh viên thành công!")

    def hien_thi_danh_sach(self):
        print("\n--- DANH SÁCH SINH VIÊN ---")
        if not self.danh_sach_sv:
            print("Danh sách trống.")
        else:
            for sv in self.danh_sach_sv:
                print(sv.hien_thi_thong_tin())

# --- CHƯƠNG TRÌNH CHÍNH ---
qlsv = QuanLySinhVien()

while True:
    print("\n=== MENU QUẢN LÝ ===")
    print("1. Thêm sinh viên")
    print("2. Hiển thị danh sách")
    print("3. Thoát")
    chon = input("Chọn chức năng (1-3): ")

    if chon == '1':
        qlsv.them_sinh_vien()
    elif chon == '2':
        qlsv.hien_thi_danh_sach()
    elif chon == '3':
        print("Kết thúc chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ!")
        