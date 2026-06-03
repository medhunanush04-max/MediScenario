import React, { useState } from 'react';

const CasesPage = () => {
  const [cases] = useState([
    { id: 1, title: 'Acute MI', difficulty: 'Hard', category: 'Cardiology', status: 'Completed', score: 85 },
    { id: 2, title: 'Diabetes Management', difficulty: 'Medium', category: 'Endocrinology', status: 'In Progress', score: null },
    { id: 3, title: 'Pneumonia', difficulty: 'Easy', category: 'Respiratory', status: 'Not Started', score: null },
  ]);

  const getDifficultyColor = (difficulty) => {
    switch (difficulty) {
      case 'Easy': return 'bg-green-100 text-green-800';
      case 'Medium': return 'bg-yellow-100 text-yellow-800';
      case 'Hard': return 'bg-red-100 text-red-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <h1 className="text-3xl font-bold text-gray-900 mb-2">Clinical Cases</h1>
      <p className="text-gray-600 mb-8">Practice clinical decision-making with AI-generated cases</p>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {cases.map((caseItem) => (
          <div key={caseItem.id} className="bg-white rounded-lg shadow-md hover:shadow-lg transition p-6">
            <div className="flex items-start justify-between mb-4">
              <h3 className="text-lg font-bold text-gray-900">{caseItem.title}</h3>
              <span className={`px-3 py-1 rounded-full text-xs font-semibold ${getDifficultyColor(caseItem.difficulty)}`}>{caseItem.difficulty}</span>
            </div>
            <p className="text-sm text-gray-600 mb-4">{caseItem.category}</p>
            <button className="w-full bg-primary-600 text-white py-2 rounded-lg hover:bg-primary-700 transition font-medium">
              {caseItem.status === 'Completed' ? 'Review' : 'Start Case'}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default CasesPage;
