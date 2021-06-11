from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    image = models.ImageField(upload_to="public/blog/images", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


STATE_CHOICE = (
 ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
 ('Andhra Pradesh','Andhra Pradesh'),
 ('Arunachal Pradesh','Arunachal Pradesh'),
 ('Assam','Assam'),
 ('Bihar','Bihar'),
 ('Chandigarh','Chandigarh'),
 ('Chhattisgarh','Chhattisgarh'),
 ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
 ('Daman and Diu','Daman and Diu'),
 ('Delhi','Delhi'),
 ('Goa','Goa'),
 ('Gujarat','Gujarat'),
 ('Haryana','Haryana'),
 ('Himachal Pradesh','Himachal Pradesh'),
 ('Jammu & Kashmir','Jammu & Kashmir'),
 ('Jharkhand','Jharkhand'),
 ('Karnataka','Karnataka'),
 ('Kerala','Kerala'),
 ('Lakshadweep','Lakshadweep'),
 ('Madhya Pradesh','Madhya Pradesh'),
 ('Maharashtra','Maharashtra'),
 ('Manipur','Manipur'),
 ('Meghalaya','Meghalaya'),
 ('Mizoram','Mizoram'),
 ('Nagaland','Nagaland'),
 ('Odisha','Odisha'),
 ('Puducherry','Puducherry'),
 ('Punjab','Punjab'),
 ('Rajasthan','Rajasthan'),
 ('Sikkim','Sikkim'),
 ('Tamil Nadu','Tamil Nadu'),
 ('Telangana','Telangana'),
 ('Tripura','Tripura'),
 ('Uttarakhand','Uttarakhand'),
 ('Uttar Pradesh','Uttar Pradesh'),
 ('West Bengal','West Bengal'),
)

class Comment(models.Model):
    blog = models.ForeignKey(Blog, null=True, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)
    country = models.CharField(max_length=100, choices=STATE_CHOICE)
    created_by = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
