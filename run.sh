#!/bin/sh

cd $0/..
source .venv/bin/activate
python SmallBlog/manage.py runserver &
cd SmallBlog/frontend 
npm run dev &
npm run tailwind
