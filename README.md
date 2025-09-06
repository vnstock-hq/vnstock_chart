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
pip install https://github.com/vnstock-hq/vnstock_chart/releases/download/vnstock_chart-1.0.0/vnstock_chart-1.0.0.tar.gz
```

## Hướng dẫn sử dụng

### Biểu đồ nến (CandleChart)

```python
from vnchart_pro import CandleChart
import pandas as pd

# Dữ liệu mẫu
df = pd.DataFrame({
    'time': pd.date_range(start='2023-01-01', periods=30),
    'open': [100, 102, ...],  # Giá mở cửa
    'high': [105, 107, ...],  # Giá cao nhất
    'low': [98, 99, ...],     # Giá thấp nhất
    'close': [103, 101, ...], # Giá đóng cửa
    'volume': [1000, 1200, ...] # Khối lượng
})

# Tạo biểu đồ nến
chart = CandleChart(
    df=df,
    mode='candle',  # 'candle' hoặc 'bar'
    title='Biểu đồ giá cổ phiếu ABC',
    theme='dark',   # 'dark' hoặc 'light'
    size_preset='medium'  # 'mini', 'small', 'medium', 'large', 'wide', 'tall'
)

# Hiển thị biểu đồ
chart.render()
```

### Biểu đồ đường (LineChart)

```python
from vnchart_pro import LineChart

# Tạo biểu đồ đường
line_chart = LineChart(
    x=df['time'].dt.strftime('%Y-%m-%d').tolist(),
    y=df['close'].tolist(),
    title='Giá đóng cửa',
    theme='light',
    color_category='positive',  # 'positive', 'negative', 'neutral'
    size_preset='medium'
)

# Hiển thị biểu đồ
line_chart.render()
```

### Biểu đồ cột (BarChart)

```python
from vnchart_pro import BarChart

# Tạo biểu đồ cột
bar_chart = BarChart(
    x=df['time'].dt.strftime('%Y-%m-%d').tolist()[-10:],
    y=df['volume'].tolist()[-10:],
    title='Khối lượng giao dịch',
    theme='dark',
    color_category='neutral',
    size_preset='medium'
)

# Hiển thị biểu đồ
bar_chart.render()
```

### Dashboard

```python
from vnchart_pro import Dashboard, LineChart, BarChart, CandleChart

# Tạo các biểu đồ riêng lẻ
candle_chart = CandleChart(df=df, mode='candle', title='Biểu đồ nến')
line_chart = LineChart(x=dates, y=closes, title='Giá đóng cửa')
bar_chart = BarChart(x=dates[-10:], y=volumes[-10:], title='Khối lượng giao dịch')

# Tạo dashboard với 3 biểu đồ
dashboard = Dashboard(
    charts=[candle_chart, line_chart, bar_chart],
    title='Phân tích thị trường',
    description='Tổng quan về diễn biến giá và khối lượng',
    theme='dark'
)

# Hiển thị dashboard với bố cục 3 panel
dashboard.layout3()
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
