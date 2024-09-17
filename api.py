from flask import Flask, request, jsonify
from network import FamilyTree

app = Flask(__name__)
family_tree = FamilyTree()

@app.route('/Member', methods=['POST'])
def Member():
    data = request.json
    member_name = data.get('fullname')
    family_tree.add_member(member_name)
    return jsonify({'message': 'Member added successfully'})

@app.route('/relationship_with', methods=['POST'])
def relationship_with():
    data = request.json
    member1 = data.get('member1')
    member2 = data.get('member2')
    relation = data.get('relation')
    family_tree.add_relationship(member1, member2, relation)
    return jsonify({'message': 'Relationship defined successfully'})

@app.route('/get_closest_relationship_degree', methods=['GET'])
def get_closest_relationship_degree():
    member1 = request.args.get('member1')
    member2 = request.args.get('member2')
    degree = family_tree.get_closest_relationship_degree(member1, member2)
    if degree is None:
        return jsonify({'error': 'No path found'}), 404
    return jsonify({'degree': degree})


if __name__ == '__main__':
    app.run(debug=True)
