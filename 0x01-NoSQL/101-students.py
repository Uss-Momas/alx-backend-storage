#!/usr/bin/env python3
"""
101-students module
"""
from typing import List


def calc_avg_score(topics: List[dict]) -> float:
    """
    calculate the average score
    """
    scores = [topic.get('score') for topic in topics]
    return sum(scores) / len(scores)


def top_students(mongo_collection):
    """
    function that returns all students sorted by average score
    """
    all_students = mongo_collection.find()
    for student in all_students:
        avg_score = calc_avg_score(student.get('topics'))
        mongo_collection.update_one({'_id': student.get('_id')}, {
                                    '$set': {'averageScore': avg_score}})

    return mongo_collection.find().sort('averageScore', -1)
