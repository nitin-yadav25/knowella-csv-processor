import pandas as pd
from django.shortcuts import render
from .forms import UploadFileForm
from .models import ProcessedData


def upload_file(request):
    message = ""

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES["file"]

            if file.name.endswith(".csv"):
                df = pd.read_csv(file)
            else:
                df = pd.read_excel(file)

            for _, row in df.iterrows():
                try:
                    ProcessedData.objects.create(
                        name=row["name"],
                        email=row["email"],
                        age=int(row["age"])
                    )
                except:
                    pass

            message = "File uploaded successfully"

    else:
        form = UploadFileForm()

    return render(request, "upload.html", {"form": form, "message": message})
    