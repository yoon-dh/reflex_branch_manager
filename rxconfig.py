import reflex as rx

config = rx.Config(
    app_name="reflex_test",
    # db_url=f"duckdb:///md:my_db?motherduck_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InZpY3Rvcnktc29vQG5hdmVyLmNvbSIsIm1kUmVnaW9uIjoiYXdzLWV1LWNlbnRyYWwtMSIsInNlc3Npb24iOiJ2aWN0b3J5LXNvby5uYXZlci5jb20iLCJwYXQiOiI2M1UyQkQ1ZzJfOXJzRHlsZXFoV3htOERHQ0xXQ3l0c21IR01taFQ5UU9RIiwidXNlcklkIjoiZWIwZmEwNGMtMzg1OC00MGVlLWIyYTYtN2IyNzQ5NjgwY2M5IiwiaXNzIjoibWRfcGF0IiwicmVhZE9ubHkiOmZhbHNlLCJ0b2tlblR5cGUiOiJyZWFkX3dyaXRlIiwiaWF0IjoxNzY4ODc1NjQzfQ._zbZ78tU-EXlSRo4Dg2VFxzGGSCd21fwm_BOC8tJ-C0",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)