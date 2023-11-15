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
                  'filename')


class SubmittedPaperSchema(Schema):
    class Meta:
        fields = ('title',
                  'authors',
                  'abstract',
                  'file',
                  'filepath',
                  'filename')


reviewed_paper_schema = ReviewedPaperSchema()
reviewed_papers_schema = ReviewedPaperSchema(many=True)
submitted_paper_schema = SubmittedPaperSchema()
submitted_papers_schema = SubmittedPaperSchema(many=True)

