# dbt & Dagster

[refer](https://docs.dagster.io/integrations/dbt)

- Dagster kết hợp với dbt giúp bạn có thể lịch lịch dbt trong một đường dẫn dữ liệu duy nhất

- Dagster hiểu dbt ở cấp độ các mô hinh dbt riêng lẻ. nghĩa là:
    + Sử dụng Dagster UI, APIs để chạy các tập hợp con của mô hình dbt, seed, snapshot.
    + Theo dõi lỗi (failures), logs và lịch sử chạy cho từng mô hình dbt, seed, snapshot
    + Xác định sự phụ thuộc giữa các mô hình dbt riêng lẻ và các asset khác.

# Getting started

- Có một số cách để bắt đầu với Dagster và dbt:

    - Làm theo [tutorial](https://docs.dagster.io/integrations/dbt/using-dbt-with-dagster): thiết lập dbt và Dagster trên máy tính của bạn thông qua [jaffle shop project](https://github.com/dbt-labs/jaffle-shop-classic) của dbt, dagster-dbt library, và một kho dữ liệu như DuckDB. Đến cuối, bạn sẽ có một dự án dbt và Dagster hoạt động và một số lượng Dagster asset được cụ thể hóa, bao gồm một biểu đồ được cung cấp bởi dữ liệu từ các mô hình dbt của bạn.
    
    - Thử nghiệm với một [dự án dbt & Dagster](https://github.com/dagster-io/dagster/tree/master/examples/assets_dbt_python) đang hoạt động để hiểu rõ hơn về cách chúng hoạt động.
    
    - Tra cứu [tài liệu tích hợp dagster-dbt](https://docs.dagster.io/integrations/dbt/reference): Tìm hiểu các bài học ngắn về các chủ đề liên quan đến dbt và Dagster.
    
    - Tra cứu [tài liệu API](https://docs.dagster.io/_apidocs/libraries/dagster-dbt) để hiểu rõ hơn về cách sử dụng và tích hợp thư viện dagster-dbt.
    
    - Tự động tải các mô hình dbt của bạn như tài sản Dagster: Bằng cách nhập một dự án dbt hiện có vào Dagster+, bạn có thể tự động chuyển các mô hình dbt của mình thành các tài sản Dagster.

# Understanding how dbt models relate to Dagster Software-defined assets

- Dagster’s software-defined assets (SDAs) có một số điểm tương đồng với dbt models.

- Software-defined asset (SDA) bao gồm 1 asset key, một tập hợp các upsteam asset keys và một thao tác chịu trách nhiệm tính toán asset từ các upstream phụ thuộc.

- Các model được xác định trong dbt project có thể được hiểu là Dagster SDA :
    - Asset key cho dbt model (theo mặc định) là tên của model.

    - Các upstream phụ thuộc của dbt model được xác định bằng các lệnh gọi ref hoặc nguồn trong định nghĩa của model.

    - Tính toán cần thiết để tính toán asset từ các upstream phụ thuộc của nó là SQL trong định nghĩa của model.

![imge1.png](/dbt_dagster/img1.png)

# Tutorial: Using dbt with Dagster

- Tích hợp dbt & dagster sử dụng jaffle shop project, dagster-dbt library, data warehouse (DuckDB).

[tutorial-dbt-dagster](/tutorial-dbt-dagster/)
