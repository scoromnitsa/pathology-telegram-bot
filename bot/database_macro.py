from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

# Database setup
DATABASE_URL = "sqlite:///test_macro.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Quiz Question Model
class QuizQuestion(Base):
    __tablename__ = "quiz_questions"
    
    id = Column(Integer, primary_key=True, index=True)
    image_path = Column(String, nullable=False)
    options_json = Column(Text, nullable=False)  # Store options as JSON
    correct_option = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)

    def get_options(self):
        return json.loads(self.options_json)

# Create the table
Base.metadata.create_all(engine)