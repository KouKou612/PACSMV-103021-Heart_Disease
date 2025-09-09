import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from Preprocessing import * 

X = df.drop("target", axis=1)
y = df["target"]

# One-hot encode categorical variables (nominal variables to 0, 1, 2 ...)
X_encoded = pd.get_dummies(X, drop_first=True)

# 20% of data set to test set
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42, stratify=y
)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


models = {
    "Logistic Regression": LogisticRegression(random_state=42, max_iter=1000),
    "Random Forest": RandomForestClassifier(random_state=42, n_estimators=100),
    "SVM": SVC(random_state=42, probability=True),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Naive Bayes": GaussianNB(),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42),
    "MLP": MLPClassifier(random_state=42, max_iter=1000),
}


# Train
results = {}
trained_models = {}

for name, model in models.items():
    # Use scaled data only for models that need it
    if name in ["Random Forest", "Decision Tree", "Gradient Boosting", "Naive Bayes"]:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
    else:
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
    
    acc = accuracy_score(y_test, y_pred)
    results[name] = acc
    trained_models[name] = model
    
    print(f"\n{name} Results:")
    print("=" * 50)
    print(f"Accuracy: {acc:.4f}")
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))


# Feature Importance (Random Forest)
rf = trained_models["Random Forest"]
feature_importance = pd.DataFrame({
    "feature": X_encoded.columns,
    "importance": rf.feature_importances_,
}).sort_values("importance", ascending=False)

plt.figure(figsize=(12, 8))
sns.barplot(x="importance", y="feature", data=feature_importance.head(20))
plt.title("Feature Importance - Random Forest", fontsize=16, fontweight="bold")
plt.xlabel("Importance", fontsize=12)
plt.ylabel("Feature", fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join("Model_Results", "Feature_Importance.png"),
            dpi=300, bbox_inches="tight")
plt.close()


# Model Comparison Plot
sorted_results = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))
plt.figure(figsize=(12, 6))
sns.barplot(x=list(sorted_results.keys()), y=list(sorted_results.values()))
plt.xticks(rotation=30)
plt.title("Model Comparison: Accuracy", fontsize=16, fontweight="bold")
plt.ylabel("Accuracy", fontsize=12)
plt.ylim(0, 1)

for i, acc in enumerate(sorted_results.values()):
    plt.text(i, acc + 0.01, f"{acc:.4f}", ha="center", va="bottom", fontweight="bold")

plt.tight_layout()
plt.savefig(os.path.join("Model_Results", "All_Model_Comparison.png"),
            dpi=300, bbox_inches="tight")
plt.close()


# Save Best Model
best_model_name = max(results, key=results.get)
best_model = trained_models[best_model_name]

joblib.dump(best_model, os.path.join("Model_Results", "best_model.pkl"))
joblib.dump(scaler, os.path.join("Model_Results", "scaler.pkl"))

print(f"\nBest model ({best_model_name}) and scaler saved to Model_Results folder")
