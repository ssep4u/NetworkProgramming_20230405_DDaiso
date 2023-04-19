# DDaiso
- **프로젝트이름/urls.py -> 앱이름/urls.py -> 앱이름/views.py -> 앱이름/models.py -> templates/앱이름/HTML파일이름.html**
- admin.py: 관리자 사이트
- form.py: 입력폼 사이트
- 개발 순서: models.py, views.py, urls.py, templates
---
1. startproject
   1. python -m pip install django~=3.2
   2. django-admin startproject DDaiso .
   3. python manage.py runserver
   4. Enable Django Support
   5. git 설정
2. startapp product
   1. python manage.py startapp product
   2. 'product', in INSTALLED_APPS in settings.py
3. product/
   1. models
      1. Product
         1. name
         2. price
         3. python manage.py makemigrations product
            - models -> DB를 만들기 위한 py 만들기
         4. python manage.py migrate product
            - DB를 만들기 위한 py -> DB 테이블 만들기
         5. \_\_str\_\_()
   2. admin
      1. Product
      2. python manage.py createsuperuser
   3. R: Product List
      1. views
         1. ProductListView
      2. urls
         1. product:list
      3. templates/product
         1. product_list.html
   4. R: Product Detail
      1. views
         1. ProductDetailView
      2. urls
         1. product:detail
      3. templates/product
         1. product_detail.html
         2. product_list.html
         ```html
         <a href="{% url 'product:detail' pk=product.id %}">{{ product.name }}</a>
         ```
   5. C: Add Product
      1. views
         1. ProductCreateView
      2. urls
         1. product:add
      3. templates/product
         1. product_create.html
         2. product_list.html
         ```html
         <a href="{% url 'product:add' %}">Add Product</a>
         ```
   6. U: ProductUpdateView
      1. views
         1. ProductUpdateView
      2. urls
         1. product:edit
      3. templates/product
         1. product_update.html
         2. product_list.html
      4. models
         1. get_absolute_url(): 수정했을 때 성공하면, model의 detail로 가는 함수
   7. D: ProductDeleteView
      1. views
         1. ProductDeleteView
      2. urls
         1. product:remove
      3. templates
         1. product_confirm_delete.html
         2. product_list.html
   8. 🐱‍🏍🎉✨💖 기능 완성