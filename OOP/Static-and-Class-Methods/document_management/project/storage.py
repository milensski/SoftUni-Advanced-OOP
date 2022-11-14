from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = list(filter(lambda c: c.id == category_id, self.categories))[0]
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = list(filter(lambda t: t.id == topic_id, self.topics))[0]
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = list(filter(lambda d: d.id == document_id, self.documents))[0]
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = list(filter(lambda c: c.id == category_id, self.categories))[0]
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = list(filter(lambda t: t.id == topic_id, self.topics))[0]
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = list(filter(lambda d: d.id == document_id, self.documents))[0]
        self.documents.remove(document)

    def get_document(self, document_id):
        document = list(filter(lambda d: d.id == document_id, self.documents))[0]
        return document

    def __repr__(self):
        return '\n'.join(map(str, self.documents))
