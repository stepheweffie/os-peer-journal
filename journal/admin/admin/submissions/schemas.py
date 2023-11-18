from flask_marshmallow import Schema


class ReviewedPaperSchema(Schema):
    class Meta:
        fields = ('title',
                  'authors',
                  'abstract',
                  'reviewed',
                  'reviewed_by',
                  'reviewed_date',
                  'review_data',
                  )


class SubmittedPaperSchema(Schema):
    class Meta:
        fields = ('id',
                  'title',
                  'authors',
                  'abstract',
                  )


class PublisheddPaperSchema(Schema):
    class Meta:
        fields = ('id',
                  'title',
                  'authors',
                  'abstract',
                  'reviewed',
                  'reviewed_by',
                  'reviewed_date',
                  'review_data',
                  'pub_date',
                  'published',
                  'published_by',
                  )


reviewed_paper_schema = ReviewedPaperSchema()
reviewed_papers_schema = ReviewedPaperSchema(many=True)
submitted_paper_schema = SubmittedPaperSchema()
submitted_papers_schema = SubmittedPaperSchema(many=True)
published_papers_schema = PublisheddPaperSchema(many=True)
