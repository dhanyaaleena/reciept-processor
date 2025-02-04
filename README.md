# Receipt Processor 

This is a **FastAPI**-based web service for processing and awarding points based on receipts.  
The application provides two endpoints:
- **Process Receipts (`POST /receipts/process`)** – Submits a receipt and returns a unique ID.
- **Get Points (`GET /receipts/{id}/points`)** – Retrieves the number of points awarded for a receipt.


## **🛠 Features**
- **Process Receipts:** Submit a receipt and get a unique ID.
- **Retrieve Points:** Fetch points awarded for a given receipt ID.
- **In-Memory Storage:** No external database is used.
- **Dockerized Setup:** Run the application seamlessly in a container.
- **Automated Setup Script:** Easily start the application using `run.sh`.

---

## **🚀 Getting Started**

### **1️⃣ Clone the Repository**
First, clone the repository from GitHub:

```sh
git clone https://github.com/dhanyaaleena/receipt-processor.git
cd receipt-processor


### **2️⃣  Execute the run.sh file**
```sh
chmod +x run.sh
./run.sh