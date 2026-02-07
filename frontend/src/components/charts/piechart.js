/**
 * PieChart Component - For showing distribution data
 */
import React from 'react';
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
} from 'chart.js';
import { Pie } from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend);

const PieChart = ({ data, title }) => {
  const chartData = {
    labels: data.labels,
    datasets: [
      {
        data: data.values,
        backgroundColor: [
          '#EC4899', // Pink for female
          '#3B82F6', // Blue for male
        ],
        borderColor: [
          '#DB2777',
          '#2563EB',
        ],
        borderWidth: 2,
        hoverOffset: 8,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'bottom',
        labels: {
          font: {
            family: 'Bricolage Grotesque, sans-serif',
            size: 13,
            weight: '500',
          },
          color: '#374151',
          padding: 15,
          usePointStyle: true,
          pointStyle: 'circle',
        },
      },
      title: {
        display: true,
        text: title,
        font: {
          size: 16,
          weight: '600',
          family: 'Bricolage Grotesque, sans-serif',
        },
        color: '#1F2937',
        padding: {
          bottom: 20,
        },
      },
      tooltip: {
        backgroundColor: 'rgba(0, 0, 0, 0.8)',
        padding: 12,
        titleFont: {
          size: 13,
          family: 'DM Mono, monospace',
        },
        bodyFont: {
          size: 14,
          family: 'Bricolage Grotesque, sans-serif',
        },
        callbacks: {
          label: function(context) {
            let label = context.label || '';
            if (label) {
              label += ': ';
            }
            label += context.parsed.toFixed(1) + '%';
            return label;
          }
        }
      },
    },
  };

  return (
    <div style={{ height: '320px', width: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <Pie data={chartData} options={options} />
    </div>
  );
};

export default PieChart;