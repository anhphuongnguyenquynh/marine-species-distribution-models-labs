#%% Load Libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import OneClassSVM
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import label_binarize
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#%% Load dataset
data_path = '../../dataset/fish_env_2022_2025.csv'
data = pd.read_csv(data_path)
print(data.columns)
print(data.head(10))

#%% Data Exploration
#Unique values

#Missing values
data.describe()
data.info()

#%% Train split test
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

#%% Data Preprocessing
# Xác định danh sách cột theo loại
cat_features = ['countryCode', 'stateProvince']
num_features = ['thetao', 'so', 'mlotst', 'uo', 'vo', 'chl', 'phyc', 'o2']

# 1. Pipeline cho cột chữ (Categorical): Điền thiếu + Mã hóa OneHot
cat_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# 2. Pipeline cho cột số (Numerical): Điền thiếu + Chuẩn hóa StandardScaler
num_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# 3. Kết hợp lại vào ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', cat_transformer, cat_features),
        ('num', num_transformer, num_features)
    ])

# 4. Tạo Pipeline tổng thể (từ tiền xử lý đến Model)
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', OneClassSVM(kernel='rbf', nu=0.1, gamma='scale'))
])

# Huấn luyện mô hình
# Lưu ý: OneClassSVM là học không giám sát, thường chỉ fit trên features
pipeline.fit(data[cat_features + num_features])

#%% Model Training
pipeline.fit(train_data)

#%% Model Evaluation
labels_binarized = label_binarize(labels_encoded, classes=range(len(label_encoder.classes_)))

# Predict the species distribution
predictions = model.decision_function(features_processed)

# Reshape predictions to match the shape of labels_binarized
predictions_reshaped = predictions.reshape(-1, 1)

auc_score = roc_auc_score(labels_binarized, predictions_reshaped, average='macro', multi_class='ovr')
print(f'Area under the ROC curve: {auc_score:.4f}')

#%% Prediction
# 5. Evaluation (Đánh giá)
# Với One-Class SVM, dự đoán 1 là "bình thường" (phù hợp), -1 là "ngoại lai"
test_preds = pipeline.predict(test_data)
# Tỷ lệ % các điểm test nằm trong vùng dự báo (Accuracy on presence)
accuracy_presence = list(test_preds).count(1) / len(test_preds)
print(f"Độ chính xác trên tập dữ liệu hiện diện: {accuracy_presence:.2%}")

# Lấy điểm số quyết định (càng cao càng phù hợp)
test_scores = pipeline.decision_function(test_data)

#%% Visualization
import seaborn as sns
import matplotlib.pyplot as plt

# Tạo DataFrame kết quả để vẽ đồ thị
results = test_data.copy()
results['suitability'] = test_scores

plt.figure(figsize=(12, 8))

# Vẽ nền các điểm khảo sát
# Màu sắc (cmap) biểu thị mức độ phù hợp: đỏ (thấp) -> vàng -> xanh (cao)
sc = plt.scatter(results['decimalLongitude'], results['decimalLatitude'], 
                 c=results['suitability'], cmap='RdYlGn', s=20, alpha=0.6)

plt.colorbar(sc, label='Chỉ số phù hợp môi trường (Suitability Index)')

# Thêm tiêu đề và nhãn
plt.title(f'Dự báo vùng phân bổ loài: {data["scientificName"].iloc[0]}', fontsize=14)
plt.xlabel('Kinh độ (Longitude)')
plt.ylabel('Vĩ độ (Latitude)')
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
# %%
