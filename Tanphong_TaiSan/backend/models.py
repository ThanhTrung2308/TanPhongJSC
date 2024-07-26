from django.db import models

class Chiphi(models.Model):
    id_chiphi = models.CharField(db_column='Id_ChiPhi', primary_key=True, max_length=100)  # Field name made lowercase.
    id_loaichiphi = models.ForeignKey('Loaichiphi', models.DO_NOTHING, db_column='Id_LoaiChiPhi')  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', max_length=100, blank=True, null=True)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', max_length=100, blank=True, null=True)  # Field name made lowercase.
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
    id_dichvu = models.BigAutoField(db_column='Id_DichVu', primary_key=True)  # Field name made lowercase.
    id_loaidichvu = models.ForeignKey('Loaidichvu', models.DO_NOTHING, db_column='Id_LoaiDichVu')  # Field name made lowercase.
    tendichvu = models.CharField(db_column='TenDichVu', max_length=100, blank=True, null=True)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngayghi = models.DateField(db_column='NgayGhi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DichVu'


class Donhang(models.Model):
    id_donhang = models.BigIntegerField(db_column='id_DonHang', primary_key=True)  # Field name made lowercase.
    ngay = models.DateTimeField(db_column='Ngay', blank=True, null=True)  # Field name made lowercase.
    id_khachhang = models.ForeignKey('Khachhang', models.DO_NOTHING, db_column='id_KhachHang', blank=True, null=True)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contractno = models.CharField(db_column='ContractNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shippingline = models.CharField(db_column='ShippingLine', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shippedper = models.CharField(db_column='ShippedPer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    portofloading = models.CharField(db_column='PortOfLoading', max_length=100, blank=True, null=True)  # Field name made lowercase.
    placeofdelivery = models.CharField(db_column='PlaceOfDelivery', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sailingon = models.CharField(db_column='SailingOn', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billofladingno = models.CharField(db_column='BillOfLadingNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    container_sealno = models.CharField(db_column='Container/SealNo', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tongsoluong = models.FloatField(db_column='TongSoLuong', blank=True, null=True)  # Field name made lowercase.
    tonggia = models.FloatField(db_column='TongGia', blank=True, null=True)  # Field name made lowercase.
    donvigiatien = models.CharField(db_column='DonViGiaTien', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bookingno = models.CharField(db_column='BookingNo', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DonHang'


class Hopdong(models.Model):
    id_hopdong = models.BigAutoField(db_column='Id_HopDong', primary_key=True)  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sohd = models.CharField(db_column='SoHD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    thoigianthue = models.BigIntegerField(db_column='ThoiGianThue', blank=True, null=True)  # Field name made lowercase.
    kythanhtoan_thang_lan_field = models.BigIntegerField(db_column='KyThanhToan(thang/lan)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tongthu = models.FloatField(db_column='TongThu', blank=True, null=True)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngayghi = models.DateField(db_column='NgayGhi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HopDong'


class HopdongDichvu(models.Model):
    id_hopdongdichvu = models.BigAutoField(db_column='Id_HopDongDichVu', primary_key=True)  # Field name made lowercase.
    id_hopdong = models.ForeignKey(Hopdong, models.DO_NOTHING, db_column='Id_HopDong', blank=True, null=True)  # Field name made lowercase.
    id_dichvu = models.ForeignKey(Dichvu, models.DO_NOTHING, db_column='Id_DichVu', blank=True, null=True)  # Field name made lowercase.
    dientich_soluong = models.FloatField(db_column='DienTich_SoLuong', blank=True, null=True)  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia', blank=True, null=True)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HopDong_DichVu'


class Khachhang(models.Model):
    id_khachhang = models.CharField(db_column='id_KhachHang', primary_key=True, max_length=100)  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', max_length=100, blank=True, null=True)  # Field name made lowercase.
    diachi = models.CharField(db_column='DiaChi', max_length=100, blank=True, null=True)  # Field name made lowercase.
    quocgia = models.CharField(db_column='QuocGia', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hoatdong = models.BigIntegerField(db_column='HoatDong', blank=True, null=True)  # Field name made lowercase.
    sdt = models.TextField(db_column='SDT', blank=True, null=True)  # Field name made lowercase.
    fax = models.TextField(db_column='FAX', blank=True, null=True)  # Field name made lowercase.
    zipcode = models.TextField(db_column='ZipCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KhachHang'


class Kheuocvay(models.Model):
    tenkheuoc = models.CharField(db_column='TenKheUoc', max_length=100)  # Field name made lowercase.
    sotienvay = models.FloatField(db_column='SoTienVay', blank=True, null=True)  # Field name made lowercase.
    laisuat_nam = models.FloatField(db_column='LaiSuat/Nam', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ngayvay = models.DateField(db_column='NgayVay', blank=True, null=True)  # Field name made lowercase.
    thoigianvay = models.CharField(db_column='ThoiGianVay', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hinhthuctravay = models.CharField(db_column='HinhThucTraVay', max_length=100, blank=True, null=True)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', max_length=100, blank=True, null=True)  # Field name made lowercase.
    makheuoc = models.CharField(db_column='MaKheUoc', max_length=100)  # Field name made lowercase.
    id_kheuoc = models.BigIntegerField(db_column='Id_KheUoc', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KheUocVay'


class Loaichiphi(models.Model):
    id_loaichiphi = models.CharField(db_column='Id_LoaiChiPhi', primary_key=True, max_length=100)  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', max_length=100)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoaiChiPhi'


class Loaidichvu(models.Model):
    id_loaidichvu = models.BigAutoField(db_column='Id_LoaiDichVu', primary_key=True)  # Field name made lowercase.
    tenloaidichvu = models.CharField(db_column='TenLoaiDichVu', max_length=100)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoaiDichVu'


class Loainguyenlieu(models.Model):
    id_loainguyenlieu = models.CharField(db_column='Id_LoaiNguyenLieu', primary_key=True, max_length=100)  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', max_length=100)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoaiNguyenLieu'


class Loaitaisan(models.Model):
    id_loaitaisan = models.BigAutoField(db_column='Id_LoaiTaiSan', primary_key=True)  # Field name made lowercase.
    tenloaitaisan = models.CharField(db_column='TenLoaiTaiSan', max_length=100)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoaiTaiSan'


class Nguyenlieu(models.Model):
    id_nguyenlieu = models.CharField(db_column='Id_NguyenLieu', primary_key=True, max_length=100)  # Field name made lowercase.
    id_loainguyenlieu = models.ForeignKey(Loainguyenlieu, models.DO_NOTHING, db_column='Id_LoaiNguyenLieu')  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gia = models.FloatField(db_column='Gia', blank=True, null=True)  # Field name made lowercase.
    xuatxu = models.CharField(db_column='XuatXu', max_length=100, blank=True, null=True)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NguyenLieu'


class Sanpham(models.Model):
    id_sanpham = models.CharField(db_column='Id_SanPham', primary_key=True, max_length=100)  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', max_length=100)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gia = models.FloatField(db_column='Gia', blank=True, null=True)  # Field name made lowercase.
    trongluong = models.FloatField(db_column='TrongLuong', blank=True, null=True)  # Field name made lowercase.
    soluongchai_thung = models.BigIntegerField(db_column='SoLuongChai/Thung', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'SanPham'


class SanphamNguyenlieu(models.Model):
    id = models.BigIntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    id_sanpham = models.ForeignKey(Sanpham, models.DO_NOTHING, db_column='Id_SanPham', blank=True, null=True)  # Field name made lowercase.
    id_nguyenlieu = models.ForeignKey(Nguyenlieu, models.DO_NOTHING, db_column='Id_NguyenLieu', blank=True, null=True)  # Field name made lowercase.
    trongluong = models.FloatField(db_column='TrongLuong', blank=True, null=True)  # Field name made lowercase.
    phantramtrongluong = models.FloatField(db_column='PhanTramTrongLuong', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SanPham_NguyenLieu'


class SanphamOld(models.Model):
    id_sanpham_old = models.CharField(db_column='Id_SanPham_Old', primary_key=True, max_length=100)  # Field name made lowercase.
    id_sanpham = models.ForeignKey(Sanpham, models.DO_NOTHING, db_column='Id_SanPham')  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', max_length=100, blank=True, null=True)  # Field name made lowercase.
    xuatxu = models.CharField(db_column='XuatXu', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SanPham_Old'


class Taisan(models.Model):
    id_taisan = models.BigAutoField(db_column='Id_TaiSan', primary_key=True)  # Field name made lowercase.
    id_loaitaisan = models.ForeignKey(Loaitaisan, models.DO_NOTHING, db_column='Id_LoaiTaiSan')  # Field name made lowercase.
    tentaisan = models.CharField(db_column='TenTaiSan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngayghitang = models.DateField(db_column='NgayGhiTang', blank=True, null=True)  # Field name made lowercase.
    thoigiansudung = models.CharField(db_column='ThoiGianSuDung', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nguyengia = models.FloatField(db_column='NguyenGia', blank=True, null=True)  # Field name made lowercase.
    chuthich = models.CharField(db_column='ChuThich', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaiSan'

class HopdongThanhtoanQuerySet(models.QuerySet):
    def search_hopdong(self, hopdong):
        return self.filter(id_hopdong = hopdong)

class HopdongThanhtoanManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return HopdongThanhtoanQuerySet(self.model, using=self._db)


class HopdongThanhtoan(models.Model):
    id = models.BigAutoField(primary_key=True)
    thoigiantao = models.DateTimeField(db_column='ThoigianTao', blank=True, null=True)  # Field name made lowercase.
    sodntt = models.CharField(db_column='SoDNTT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sotbdv = models.CharField(db_column='SoTBDV', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id_hopdong = models.ForeignKey(Hopdong, models.DO_NOTHING, db_column='Id_HopDong', blank=True, null=True, related_name='hopdong_thanhtoan')  # Field name made lowercase.
    giamtru = models.FloatField(db_column='GiamTru', blank=True, null=True)  # Field name made lowercase.
    tongtientruocthue = models.FloatField(db_column='TongTienTruocThue', blank=True, null=True)  # Field name made lowercase.
    tongtiensauthue = models.FloatField(db_column='TongTienSauThue', blank=True, null=True)  # Field name made lowercase.

    objects = HopdongThanhtoanManager()
    class Meta:
        managed = False
        db_table = 'HopDong_ThanhToan'

class Thanhtoan(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dichvu = models.ForeignKey(Dichvu, models.DO_NOTHING, db_column='DichVu', blank=True, null=True)  # Field name made lowercase.
    tientruocthue = models.FloatField(db_column='TienTruocThue', blank=True, null=True)  # Field name made lowercase.
    thue = models.FloatField(db_column='Thue', blank=True, null=True)  # Field name made lowercase.
    tiensauthue = models.FloatField(db_column='TienSauThue', blank=True, null=True)  # Field name made lowercase.
    donvitinh = models.CharField(db_column='DonViTinh', max_length=100, blank=True, null=True)  # Field name made lowercase.
    chisocu = models.IntegerField(db_column='ChiSoCu', blank=True, null=True)  # Field name made lowercase.
    chisomoi = models.IntegerField(db_column='ChiSoMoi', blank=True, null=True)  # Field name made lowercase.
    heso = models.IntegerField(db_column='HeSo', blank=True, null=True)  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia', blank=True, null=True)  # Field name made lowercase.
    sosudung = models.FloatField(db_column='SoSuDung', blank=True, null=True)  # Field name made lowercase.
    loaithue = models.BigIntegerField(db_column='LoaiThue', blank=True, null=True)  # Field name made lowercase.
    id_hopdongthanhtoan = models.ForeignKey(HopdongThanhtoan, models.DO_NOTHING, db_column='Id_HopDongThanhToan', blank=True, null=True, related_name='thanhtoan')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ThanhToan'


class TuybienChiphi(models.Model):
    id_khachhang = models.ForeignKey(Khachhang, models.DO_NOTHING, db_column='id_KhachHang')  # Field name made lowercase.
    id_chiphi = models.ForeignKey(Chiphi, models.DO_NOTHING, db_column='id_ChiPhi', blank=True, null=True)  # Field name made lowercase.
    id_tuybien_chiphi = models.BigIntegerField(db_column='Id_Tuybien_Chiphi', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TuyBien_ChiPhi'