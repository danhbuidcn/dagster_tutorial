## Creating hello_dagster project

```
mkdir hello_dagster
cd hello_dagster
touch hello_dagster.py
pip install pandas

dagster dev -f hello_dagster.py -p 3001
```

- Tạo một project cơ bản để build một data pipeline với các giai đoạn:
  - Downloads top 10 stories từ HackerNews
  - Tiến hành lọc và chọn ra các field cần thiết
  - Ghi kết quả thu được vào Pandas Dataframe rồi cuối cùng lưu xuống file .csv

- Ở đoạn code trên, chúng ta define 2 function:
  - hackernews_top_story_ids có nhiệm vụ fetch data (ID của các story) từ API của Hacker News, sau đó lưu vào file dưới dạng JSON
  - hackernews_top_stories sẽ đọc dữ liệu từ file JSON vừa lưu, sau đó tiếp tục collect data (dựa trên iD vừa thu được) và lưu vào một Pandas Dataframe.

- Thêm decorator @asset cho mỗi function. 
  - Và từ đó chúng ta đã có 2 assets lần lượt là hackernews_top_story_ids và hackernews_top_stoies.
  - Ở decorator của function hackernews_top_stories có tham số deps, có nghĩa là asset hackernews_top_stoies phụ thuộc vào asset hackernews_top_story_ids

- Thông tin của asset sẽ được lưu trong metadata. Ở trong hàm hackernews_top_stories ta đã định nghĩa metadata và lưu các thông tin cơ bản của asset trong đó.
