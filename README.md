# Vnstock Chart

<div align="center">
  <img src="https://vnstocks.com/_next/image?url=%2Fimg%2Fvnstock_logo_trans_rec_hoz.png&w=256&q=75" alt="VnChartPro Logo" width="300">
  <h3>Thư viện trực quan hóa dữ liệu tài chính chuyên nghiệp cho thị trường chứng khoán Việt Nam</h3>
</div>

## Giới thiệu

VnChartPro là thư viện trực quan hóa dữ liệu tài chính chuyên nghiệp được phát triển bởi [VnStock](https://vnstocks.com), được thiết kế đặc biệt cho phân tích thị trường chứng khoán Việt Nam. Thư viện cung cấp các công cụ tạo biểu đồ tương tác, đẹp mắt và dễ sử dụng, hoạt động liền mạch trong nhiều môi trường khác nhau như Jupyter Notebook, Google Colab, VS Code và các ứng dụng web.

### Tính năng nổi bật

- **Đa dạng biểu đồ**: Hỗ trợ nhiều loại biểu đồ tài chính phổ biến (nến, đường, cột, scatter, boxplot, heatmap...)
- **Tương thích đa nền tảng**: Hoạt động mượt mà trong Jupyter, Google Colab, VS Code và ứng dụng web
- **Giao diện chuyên nghiệp**: Các chủ đề và bảng màu được thiết kế tinh tế cho phân tích tài chính
- **Tùy biến linh hoạt**: Dễ dàng điều chỉnh kích thước, màu sắc, và các thông số khác
- **Dashboard tích hợp**: Tạo bảng điều khiển với nhiều biểu đồ trong vài dòng code
- **Tối ưu hiệu suất**: Xử lý hiệu quả các tập dữ liệu lớn

## Cài đặt

```bash
pip install https://github.com/vnstock-hq/vnstock_chart/releases/download/1.0.0/vnstock_chart-1.0.0.tar.gz
```

## Hướng dẫn sử dụng

### Dữ liệu mẫu 

```python
import pandas as pd
from vnstock import Quote

quote = Quote(symbol='VCI', source='TCBS')
df = quote.history(start='2020-01-01', end='2024-05-25', interval='1D')
df['time'] = pd.to_datetime(df['time'])
df = df.sort_values('time')
df
```

### Biểu đồ nến (CandleChart)

```python
from vnchart_pro import CandleChart
CandleChart(
    df=df,
    mode="price",
    title="VCI Close Price + Volume",
    size_preset='large'
).render()
```

### Biểu đồ đường (LineChart)

```python
from vnchart_pro import LineChart

dates = df['time'].dt.strftime('%Y-%m-%d').tolist()
closes = df['close'].tolist()

lc = LineChart(
    x=dates,
    y=closes,
    title="Close Price",
    theme="light",
    color_category="positive",
    size_preset='medium',
    watermark=True
)
lc.render()
```

### Biểu đồ cột (BarChart)

```python
from vnchart_pro import BarChart

dates  = df['time'].dt.strftime('%Y-%m-%d').tolist()
vols   = df['volume'].tolist()

bc = BarChart(
    x=dates,
    y=vols,
    title="VCI Daily Volume",
    theme="light",
    color_category="neutral",
    watermark=True,
    size_preset='medium'
)
bc.render()
```

## Các loại biểu đồ hỗ trợ

- **CandleChart**: Biểu đồ nến và biểu đồ OHLC
- **LineChart**: Biểu đồ đường
- **BarChart**: Biểu đồ cột
- **ScatterChart**: Biểu đồ phân tán
- **BoxplotChart**: Biểu đồ hộp
- **HeatmapChart**: Biểu đồ nhiệt

## Tùy chỉnh giao diện

### Chủ đề (Theme)

```python
# Chủ đề tối
chart = LineChart(..., theme='dark')

# Chủ đề sáng
chart = LineChart(..., theme='light')
```

### Kích thước (Size Preset)

```python
# Các kích thước có sẵn
chart = LineChart(..., size_preset='mini')    # 300x200
chart = LineChart(..., size_preset='small')   # 450x300
chart = LineChart(..., size_preset='medium')  # 600x400
chart = LineChart(..., size_preset='large')   # 800x500
chart = LineChart(..., size_preset='wide')    # 900x400
chart = LineChart(..., size_preset='tall')    # 600x600

# Hoặc tùy chỉnh kích thước
chart = LineChart(..., width=700, height=350)
```

### Màu sắc (Color Category)

```python
# Màu tích cực (xanh lá)
chart = LineChart(..., color_category='positive')

# Màu tiêu cực (đỏ)
chart = LineChart(..., color_category='negative')

# Màu trung tính (xanh dương)
chart = LineChart(..., color_category='neutral')
```

## Xuất biểu đồ

```python
# Xuất ra file HTML
chart.to_html('chart.html')

# Lấy HTML snippet để nhúng vào web
html_snippet = chart.embed()
```

## Yêu cầu hệ thống

- Python 3.10 trở lên
- Các thư viện phụ thuộc: pandas, pyecharts, panel

## Tài liệu tham khảo

Xem thêm các ví dụ chi tiết trong [notebook demo](./vnchart_pro_demo.ipynb).

## Liên hệ và hỗ trợ

- Website: [https://vnstocks.com](https://vnstocks.com)
- Email: support@vnstocks.com
- GitHub: [https://github.com/vnstock-hq/vnchart_pro](https://github.com/vnstock-hq/vnchart_pro)

## Giấy phép

VnChartPro được phát hành dưới giấy phép MIT.
