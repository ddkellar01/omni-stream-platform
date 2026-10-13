import React, { useState } from 'react';
import { Share2, Video, Send, CheckCircle2 } from 'lucide-react';

export default function App() {
  const [platforms, setPlatforms] = useState({
    youtube: true,
    instagram: true,
    facebook: true,
    snapchat: false,
    x: true,
  });
  const [caption, setCaption] = useState('');
  const [status, setStatus] = useState('');

  const handlePublish = async () => {
    setStatus('Publishing across selected channels...');
    const selected = Object.keys(platforms).filter(k => platforms[k as keyof typeof platforms]);
    
    // Call API Gateway promotion endpoint
    setTimeout(() => {
      setStatus(`Successfully queued promotion for: ${selected.join(', ')}!`);
    }, 1200);
  };

  return (
    <div style={{ background: '#0f172a', color: '#f8fafc', minHeight: '100vh', padding: '40px', fontFamily: 'sans-serif' }}>
      <div style={{ maxWidth: '600px', margin: '0 auto', background: '#1e293b', padding: '30px', borderRadius: '12px', boxShadow: '0 10px 25px rgba(0,0,0,0.3)' }}>
        <h2 style={{ display: 'flex', alignItems: 'center', gap: '10px' }}><Share2 /> OmniStream Publisher Dashboard</h2>
        <p style={{ color: '#94a3b8' }}>Simultaneously blast your video content and vertical shorts to all major networks.</p>
        
        <div style={{ margin: '20px 0' }}>
          <label style={{ display: 'block', marginBottom: '8px', fontWeight: 'bold' }}>Video Caption / Metadata</label>
          <textarea 
            rows={3} 
            value={caption} 
            onChange={(e) => setCaption(e.target.value)}
            placeholder="Write your cross-platform caption or hook here..."
            style={{ width: '100%', padding: '10px', borderRadius: '6px', background: '#0f172a', border: '1px solid #334155', color: '#fff' }}
          />
        </div>

        <div style={{ margin: '20px 0' }}>
          <label style={{ display: 'block', marginBottom: '10px', fontWeight: 'bold' }}>Target Channels</label>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
            {Object.keys(platforms).map(p => (
              <label key={p} style={{ display: 'flex', alignItems: 'center', gap: '8px', textTransform: 'capitalize', cursor: 'pointer' }}>
                <input 
                  type="checkbox" 
                  checked={platforms[p as keyof typeof platforms]} 
                  onChange={() => setPlatforms({...platforms, [p]: !platforms[p as keyof typeof platforms]})}
                />
                {p}
              </label>
            ))}
          </div>
        </div>

        <button 
          onClick={handlePublish}
          style={{ width: '100%', background: '#3b82f6', color: '#fff', border: 'none', padding: '12px', borderRadius: '6px', fontWeight: 'bold', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px' }}
        >
          <Send size={18} /> Publish Across Channels
        </button>

        {status && (
          <div style={{ marginTop: '20px', padding: '10px', background: '#065f46', borderRadius: '6px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <CheckCircle2 size={18} /> {status}
          </div>
        )}
      </div>
    </div>
  );
}
