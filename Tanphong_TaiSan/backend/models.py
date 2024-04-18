from django.db import models

# Create your models here.

class Chiphi(models.Model):
    id_chiphi = models.CharField(db_column='Id_ChiPhi', primary_key=True)  # Field name made lowercase.
    id_loaichiphi = models.ForeignKey('Loaichiphi', models.DO_NOTHING, db_column='Id_LoaiChiPhi')  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', blank=True, null=True)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', blank=True, null=True)  # Field name made lowercase.
    gia = models.FloatField(db_column='Gia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChiPhi'


class Chitietdonhang(models.Model):
    id_chitietdonhang = models.BigIntegerField(db_column='id_ChiTietDonHang', primary_key=True)  # Field name made lowercase.
    id_donhang = models.ForeignKey('Donhang', models.DO_NOTHING, db_column='Id_DonHang', blank=True, null=True)  # Field name made lowercase.
    id_sanpham = models.ForeignKey('Sanpham', models.DO_NOTHING, db_column='Id_SanPham', blank=True, null=True)  # Field name made lowercase.
    trongluongnet_kg_field = models.FloatField(db_column='TrongLuongNet(KG)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    trongluonggross_kg_field = models.FloatField(db_column='TrongLuongGross(KG)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    trongluongnet_chai_kg_field = models.FloatField(db_column='TrongLuongNet/Chai(KG)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    soluongthung = models.FloatField(db_column='SoLuongThung', blank=True, null=True)  # Field name made lowercase.
    giasanpham_kg = models.FloatField(db_column='GiaSanPham/KG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    soluongchai = models.BigIntegerField(db_column='SoLuongChai', blank=True, null=True)  # Field name made lowercase.
    trongluongnet_thung_kg_field = models.FloatField(db_column='TrongLuongNet/Thung(KG)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.       
    trongluonggross_thung_kg_field = models.FloatField(db_column='TrongLuongGross/Thung(KG)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.   
    tonggiasanpham = models.FloatField(db_column='TongGiaSanPham', blank=True, null=True)  # Field name made lowercase.
    soluongchai_thung = models.IntegerField(db_column='SoLuongChai/Thung', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'ChiTietDonHang'


class Dichvu(models.Model):
    id_dichvu = models.CharField(db_column='Id_DichVu', primary_key=True)  # Field name made lowercase.
    id_loaidichvu = models.ForeignKey('Loaidichvu', models.DO_NOTHING, db_column='Id_LoaiDichVu')  # Field name made lowercase.
    tendichvu = models.CharField(db_column='TenDichVu', blank=True, null=True)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DichVu'


class Donhang(models.Model):
    id_donhang = models.BigIntegerField(db_column='id_DonHang', primary_key=True)  # Field name made lowercase.
    ngay = models.DateTimeField(db_column='Ngay', blank=True, null=True)  # Field name made lowercase.
    id_khachhang = models.ForeignKey('Khachhang', models.DO_NOTHING, db_column='id_KhachHang', blank=True, null=True)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', blank=True, null=True)  # Field name made lowercase.
    contractno = models.CharField(db_column='ContractNo', blank=True, null=True)  # Field name made lowercase.
    shippingline = models.CharField(db_column='ShippingLine', blank=True, null=True)  # Field name made lowercase.
    shippedper = models.CharField(db_column='ShippedPer', blank=True, null=True)  # Field name made lowercase.
    portofloading = models.CharField(db_column='PortOfLoading', blank=True, null=True)  # Field name made lowercase.
    placeofdelivery = models.CharField(db_column='PlaceOfDelivery', blank=True, null=True)  # Field name made lowercase.
    sailingon = models.CharField(db_column='SailingOn', blank=True, null=True)  # Field name made lowercase.
    billofladingno = models.CharField(db_column='BillOfLadingNo', blank=True, null=True)  # Field name made lowercase.
    container_sealno = models.CharField(db_column='Container/SealNo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tongsoluong = models.FloatField(db_column='TongSoLuong', blank=True, null=True)  # Field name made lowercase.
    tonggia = models.FloatField(db_column='TongGia', blank=True, null=True)  # Field name made lowercase.
    donvigiatien = models.CharField(db_column='DonViGiaTien', blank=True, null=True)  # Field name made lowercase.
    bookingno = models.CharField(db_column='BookingNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DonHang'


class Hopdong(models.Model):
    id_hopdong = models.CharField(db_column='Id_HopDong', primary_key=True)  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', blank=True, null=True)  # Field name made lowercase.
    sohd = models.CharField(db_column='SoHD', blank=True, null=True)  # Field name made lowercase.
    thoigianthue = models.BigIntegerField(db_column='ThoiGianThue', blank=True, null=True)  # Field name made lowercase.
    kythanhtoan_thang_lan_field = models.BigIntegerField(db_column='KyThanhToan(thang/lan)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.    
    tongthu = models.FloatField(db_column='TongThu', blank=True, null=True)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HopDong'


class HopdongDichvu(models.Model):
    id_hopdongdichvu = models.CharField(db_column='Id_HopDongDichVu', primary_key=True)  # Field name made lowercase.
    id_hopdong = models.ForeignKey(Hopdong, models.DO_NOTHING, db_column='Id_HopDong')  # Field name made lowercase.
    id_dichvu = models.ForeignKey(Dichvu, models.DO_NOTHING, db_column='Id_DichVu', blank=True, null=True)  # Field name made lowercase.
    dientich_soluong = models.FloatField(db_column='DienTich_SoLuong', blank=True, null=True)  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia', blank=True, null=True)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HopDong_DichVu'


class Khachhang(models.Model):
    id_khachhang = models.CharField(db_column='id_KhachHang', primary_key=True)  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', blank=True, null=True)  # Field name made lowercase.
    diachi = models.CharField(db_column='DiaChi', blank=True, null=True)  # Field name made lowercase.
    quocgia = models.CharField(db_column='QuocGia', blank=True, null=True)  # Field name made lowercase.
    hoatdong = models.BigIntegerField(db_column='HoatDong', blank=True, null=True)  # Field name made lowercase.
    sdt = models.TextField(db_column='SDT', blank=True, null=True)  # Field name made lowercase.
    fax = models.TextField(db_column='FAX', blank=True, null=True)  # Field name made lowercase.
    zipcode = models.TextField(db_column='ZipCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KhachHang'


class Kheuocvay(models.Model):
    id_kheuoc = models.AutoField(db_column='Id_KheUoc', primary_key=True)  # Field name made lowercase.
    tenkheuoc = models.CharField(db_column='TenKheUoc')  # Field name made lowercase.
    sotienvay = models.FloatField(db_column='SoTienVay', blank=True, null=True)  # Field name made lowercase.
    laisuat_nam = models.FloatField(db_column='LaiSuat/Nam', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ngayvay = models.DateField(db_column='NgayVay', blank=True, null=True)  # Field name made lowercase.
    thoigianvay = models.CharField(db_column='ThoiGianVay', blank=True, null=True)  # Field name made lowercase.
    hinhthuctravay = models.CharField(db_column='HinhThucTraVay', blank=True, null=True)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KheUocVay'


class Loaichiphi(models.Model):
    id_loaichiphi = models.CharField(db_column='Id_LoaiChiPhi', primary_key=True)  # Field name made lowercase.
    ten = models.CharField(db_column='Ten')  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoaiChiPhi'


class Loaidichvu(models.Model):
    id_loaidichvu = models.CharField(db_column='Id_LoaiDichVu', primary_key=True)  # Field name made lowercase.
    tenloaidichvu = models.CharField(db_column='TenLoaiDichVu')  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoaiDichVu'


class Loainguyenlieu(models.Model):
    id_loainguyenlieu = models.CharField(db_column='Id_LoaiNguyenLieu', primary_key=True)  # Field name made lowercase.
    ten = models.CharField(db_column='Ten')  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoaiNguyenLieu'


class Loaitaisan(models.Model):
    id_loaitaisan = models.CharField(db_column='Id_LoaiTaiSan', primary_key=True)  # Field name made lowercase.
    tenloaitaisan = models.CharField(db_column='TenLoaiTaiSan')  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoaiTaiSan'


class Nguyenlieu(models.Model):
    id_nguyenlieu = models.CharField(db_column='Id_NguyenLieu', primary_key=True)  # Field name made lowercase.
    id_loainguyenlieu = models.ForeignKey(Loainguyenlieu, models.DO_NOTHING, db_column='Id_LoaiNguyenLieu')  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', blank=True, null=True)  # Field name made lowercase.
    gia = models.FloatField(db_column='Gia', blank=True, null=True)  # Field name made lowercase.
    xuatxu = models.CharField(db_column='XuatXu', blank=True, null=True)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NguyenLieu'


class Sanpham(models.Model):
    id_sanpham = models.CharField(db_column='Id_SanPham', primary_key=True)  # Field name made lowercase.
    ten = models.CharField(db_column='Ten')  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SanPham'


class SanphamNguyenlieu(models.Model):
    id = models.BigIntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    id_sanpham = models.ForeignKey(Sanpham, models.DO_NOTHING, db_column='Id_SanPham', blank=True, null=True)  # Field name made lowercase.
    id_nguyenlieu = models.ForeignKey(Nguyenlieu, models.DO_NOTHING, db_column='Id_NguyenLieu', blank=True, null=True)  # Field name made lowercase.
    trongluong = models.FloatField(db_column='TrongLuong', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SanPham_NguyenLieu'


class SanphamOld(models.Model):
    id_sanpham_old = models.CharField(db_column='Id_SanPham_Old', primary_key=True)  # Field name made lowercase.
    id_sanpham = models.ForeignKey(Sanpham, models.DO_NOTHING, db_column='Id_SanPham')  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', blank=True, null=True)  # Field name made lowercase.
    xuatxu = models.CharField(db_column='XuatXu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SanPham_Old'


class Taisan(models.Model):
    id_taisan = models.BigAutoField(db_column='Id_TaiSan', primary_key=True)  # Field name made lowercase.
    id_loaitaisan = models.ForeignKey(Loaitaisan, models.DO_NOTHING, db_column='Id_LoaiTaiSan')  # Field name made lowercase.
    tenloaitaisan = models.CharField(db_column='TenLoaiTaiSan', blank=True, null=True)  # Field name made lowercase.
    ngayghitang = models.DateField(db_column='NgayGhiTang', blank=True, null=True)  # Field name made lowercase.
    thoigiansudung = models.CharField(db_column='ThoiGianSuDung', blank=True, null=True)  # Field name made lowercase.
    nguyengia = models.FloatField(db_column='NguyenGia', blank=True, null=True)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaiSan'


class TuybienChiphi(models.Model):
    id_khachhang = models.ForeignKey(Khachhang, models.DO_NOTHING, db_column='id_KhachHang')  # Field name made lowercase.
    id_chiphi = models.ForeignKey(Chiphi, models.DO_NOTHING, db_column='id_ChiPhi', blank=True, null=True)  # Field name made lowercase.
    id_tuybien_chiphi = models.BigIntegerField(db_column='Id_Tuybien_Chiphi', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TuyBien_ChiPhi'


class AuthGroup(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40, blank=True, null=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'