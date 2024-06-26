# Generated by Django 5.0.4 on 2024-04-15 09:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('name_af', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ar', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ar_dz', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ast', models.CharField(max_length=100, null=True, unique=True)),
                ('name_az', models.CharField(max_length=100, null=True, unique=True)),
                ('name_bg', models.CharField(max_length=100, null=True, unique=True)),
                ('name_be', models.CharField(max_length=100, null=True, unique=True)),
                ('name_bn', models.CharField(max_length=100, null=True, unique=True)),
                ('name_br', models.CharField(max_length=100, null=True, unique=True)),
                ('name_bs', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ca', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ckb', models.CharField(max_length=100, null=True, unique=True)),
                ('name_cs', models.CharField(max_length=100, null=True, unique=True)),
                ('name_cy', models.CharField(max_length=100, null=True, unique=True)),
                ('name_da', models.CharField(max_length=100, null=True, unique=True)),
                ('name_de', models.CharField(max_length=100, null=True, unique=True)),
                ('name_dsb', models.CharField(max_length=100, null=True, unique=True)),
                ('name_el', models.CharField(max_length=100, null=True, unique=True)),
                ('name_en', models.CharField(max_length=100, null=True, unique=True)),
                ('name_en_au', models.CharField(max_length=100, null=True, unique=True)),
                ('name_en_gb', models.CharField(max_length=100, null=True, unique=True)),
                ('name_eo', models.CharField(max_length=100, null=True, unique=True)),
                ('name_es', models.CharField(max_length=100, null=True, unique=True)),
                ('name_es_ar', models.CharField(max_length=100, null=True, unique=True)),
                ('name_es_co', models.CharField(max_length=100, null=True, unique=True)),
                ('name_es_mx', models.CharField(max_length=100, null=True, unique=True)),
                ('name_es_ni', models.CharField(max_length=100, null=True, unique=True)),
                ('name_es_ve', models.CharField(max_length=100, null=True, unique=True)),
                ('name_et', models.CharField(max_length=100, null=True, unique=True)),
                ('name_eu', models.CharField(max_length=100, null=True, unique=True)),
                ('name_fa', models.CharField(max_length=100, null=True, unique=True)),
                ('name_fi', models.CharField(max_length=100, null=True, unique=True)),
                ('name_fr', models.CharField(max_length=100, null=True, unique=True)),
                ('name_fy', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ga', models.CharField(max_length=100, null=True, unique=True)),
                ('name_gd', models.CharField(max_length=100, null=True, unique=True)),
                ('name_gl', models.CharField(max_length=100, null=True, unique=True)),
                ('name_he', models.CharField(max_length=100, null=True, unique=True)),
                ('name_hi', models.CharField(max_length=100, null=True, unique=True)),
                ('name_hr', models.CharField(max_length=100, null=True, unique=True)),
                ('name_hsb', models.CharField(max_length=100, null=True, unique=True)),
                ('name_hu', models.CharField(max_length=100, null=True, unique=True)),
                ('name_hy', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ia', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ind', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ig', models.CharField(max_length=100, null=True, unique=True)),
                ('name_io', models.CharField(max_length=100, null=True, unique=True)),
                ('name_is', models.CharField(max_length=100, null=True, unique=True)),
                ('name_it', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ja', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ka', models.CharField(max_length=100, null=True, unique=True)),
                ('name_kab', models.CharField(max_length=100, null=True, unique=True)),
                ('name_kk', models.CharField(max_length=100, null=True, unique=True)),
                ('name_km', models.CharField(max_length=100, null=True, unique=True)),
                ('name_kn', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ko', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ky', models.CharField(max_length=100, null=True, unique=True)),
                ('name_lb', models.CharField(max_length=100, null=True, unique=True)),
                ('name_lt', models.CharField(max_length=100, null=True, unique=True)),
                ('name_lv', models.CharField(max_length=100, null=True, unique=True)),
                ('name_mk', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ml', models.CharField(max_length=100, null=True, unique=True)),
                ('name_mn', models.CharField(max_length=100, null=True, unique=True)),
                ('name_mr', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ms', models.CharField(max_length=100, null=True, unique=True)),
                ('name_my', models.CharField(max_length=100, null=True, unique=True)),
                ('name_nb', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ne', models.CharField(max_length=100, null=True, unique=True)),
                ('name_nl', models.CharField(max_length=100, null=True, unique=True)),
                ('name_nn', models.CharField(max_length=100, null=True, unique=True)),
                ('name_os', models.CharField(max_length=100, null=True, unique=True)),
                ('name_pa', models.CharField(max_length=100, null=True, unique=True)),
                ('name_pl', models.CharField(max_length=100, null=True, unique=True)),
                ('name_pt', models.CharField(max_length=100, null=True, unique=True)),
                ('name_pt_br', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ro', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ru', models.CharField(max_length=100, null=True, unique=True)),
                ('name_sk', models.CharField(max_length=100, null=True, unique=True)),
                ('name_sl', models.CharField(max_length=100, null=True, unique=True)),
                ('name_sq', models.CharField(max_length=100, null=True, unique=True)),
                ('name_sr', models.CharField(max_length=100, null=True, unique=True)),
                ('name_sr_latn', models.CharField(max_length=100, null=True, unique=True)),
                ('name_sv', models.CharField(max_length=100, null=True, unique=True)),
                ('name_sw', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ta', models.CharField(max_length=100, null=True, unique=True)),
                ('name_te', models.CharField(max_length=100, null=True, unique=True)),
                ('name_tg', models.CharField(max_length=100, null=True, unique=True)),
                ('name_th', models.CharField(max_length=100, null=True, unique=True)),
                ('name_tk', models.CharField(max_length=100, null=True, unique=True)),
                ('name_tr', models.CharField(max_length=100, null=True, unique=True)),
                ('name_tt', models.CharField(max_length=100, null=True, unique=True)),
                ('name_udm', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ug', models.CharField(max_length=100, null=True, unique=True)),
                ('name_uk', models.CharField(max_length=100, null=True, unique=True)),
                ('name_ur', models.CharField(max_length=100, null=True, unique=True)),
                ('name_uz', models.CharField(max_length=100, null=True, unique=True)),
                ('name_vi', models.CharField(max_length=100, null=True, unique=True)),
                ('name_zh_hans', models.CharField(max_length=100, null=True, unique=True)),
                ('name_zh_hant', models.CharField(max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_type', models.CharField(choices=[('article', 'Article'), ('news', 'News')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_af', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ar_dz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ast', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_az', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_be', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_bg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_bn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_br', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_bs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ca', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ckb', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_cs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_cy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_da', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_de', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_dsb', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_el', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_en', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_en_au', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_en_gb', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_eo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_es', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_es_ar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_es_co', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_es_mx', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_es_ni', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_es_ve', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_et', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_eu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_fa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_fi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_fr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_fy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_gd', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_gl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_he', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_hi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_hr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_hsb', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_hu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_hy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ig', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ind', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_io', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_is', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_it', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ja', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ka', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_kab', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_kk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_km', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_kn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ko', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ky', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_lb', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_lt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_lv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_mk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ml', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_mn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_mr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ms', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_my', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_nb', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ne', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_nl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_nn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_os', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_pa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_pl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_pt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_pt_br', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ru', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_sk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_sl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_sq', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_sr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_sr_latn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_sv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_sw', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_te', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_tg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_th', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_tk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_tr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_tt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_udm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ug', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_uk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_ur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_uz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_vi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_zh_hans', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
                ('author_zh_hant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.author')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.post')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post')),
            ],
        ),
    ]
