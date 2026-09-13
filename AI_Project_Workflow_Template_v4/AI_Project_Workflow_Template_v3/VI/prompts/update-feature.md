# Prompt — Cập Nhật Feature

Trace feature hiện tại theo UI → API → service/domain → database → tests.

Không mặc định implementation hiện tại là đúng. Xác định behavior cần đổi, compatibility impact, test bị ảnh hưởng và có cần migration không.

Implement thay đổi nhỏ nhất an toàn và verify tất cả layer bị ảnh hưởng.
